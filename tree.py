import re, uuid, sys
from datetime import datetime, timedelta
from host import THost
from pattern import TPattern

space_characters = [' ','\t','\n','\r']

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf_vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b[a-zA-Z_\':,]+[\s(){}\[\]=.]')

class Tree:

    def __init__(self):
        self.patterns = {}
        self.patterns_indexes = {}
        self.tfidf_matrix = None
        self.vectors = None

    def add_pattern(self, pattern):
        hash_value = hash(pattern.text) & sys.maxint
        if hash_value not in self.patterns:
            self.patterns.update({hash_value: pattern})
            patterns = self.patterns.values()
            documents = [ p.text for p in patterns ]
            self.tfidf_matrix = tfidf_vectorizer.fit(documents)
            self.vectors = self.tfidf_matrix.transform(documents)
            self.patterns_indexes = dict(enumerate(patterns))
        return hash_value

    def clear(self):
        self.patterns = {}

    def put(self, data):
        parts = []
        word = []
        meet_square_bracket = False
        parts_count = 0
        c_count = 0
        for c in data:
            c_count +=1
            if c == '[':
                meet_square_bracket = True
            if c == ']':
                meet_square_bracket = False
            if c in space_characters and not meet_square_bracket:
                parts.append(''.join(word))
                word = []
                parts_count += 1
                if parts_count == 5:
                    break
            else:
                word.append(c)

        parts.append(data[c_count:])

        if len(parts) > 4:
            level = parts[0]
            host = parts[4]
            text = " ".join((parts[5:]))
            ts = datetime.strptime("%s %s" % (parts[1], parts[2]), "%Y-%m-%d %H:%M:%S,%f")
            ts_string = "".join([parts[1], " ", parts[2]])
            data_dict = {'level':level, 'host':host, 'text': text, 'ts':ts, 'id': uuid.uuid4(), 'ts_string':ts_string, 'message_lines': text.split('\n') }
            self.process_data_dict(data_dict)

        return datetime.now().date().strftime("%Y-%m-%d")

    def process_data_dict(self, data_dict):
        if self.tfidf_matrix:
            vectors = self.tfidf_matrix.transform([data_dict['text']])
            similarities = cosine_similarity(self.vectors, vectors)
            max_similarity = -1
            max_similarity_index = -1
            for i, s in enumerate(similarities):
                if s[0] > max_similarity:
                    max_similarity = s[0]
                    max_similarity_index = i

            if max_similarity > 0.84:
                pattern = self.patterns_indexes[max_similarity_index]
                pattern.put(data_dict)
                return

        new_pattern = TPattern(data_dict)
        new_pattern.put(data_dict)
        self.add_pattern(new_pattern)

    def get_digest(self, time_deltas):
        digest = []
        now = datetime.now()
        total_patterns = 0
        zero_patterns = 0
        for hash in self.patterns:
            pattern = self.patterns[hash]
            counts, total = pattern.get_counts(time_deltas)
            digest.append({'message_lines': pattern.message_lines, 'total': total, 'counts': counts, 'hash': hash, 'last_ts_delta': pattern.get_last_ts_delta(now), 'id': pattern.id })
            if total == 0:
                zero_patterns += 1
        digest.sort(key=lambda p: p['counts'][0]['count'], reverse=True)
        return {'digest':digest, 'zero_patterns': zero_patterns, 'total_patterns': len(digest)}

    def get_host_data(self, hash, host, td):
        return {'data': self.patterns[hash].get_data(host, td)}

    def get_details(self, hash, td):
        pattern = self.patterns[hash]
        pattern_details = pattern.get_details(td)
        if pattern_details["count"] > 0:
            data_count = pattern_details["count"]
            if data_count > 10:
                data_count = 10
            data = [ item for item in self.patterns[hash].latest_data if item['ts'] > td ]
            data.reverse()
            return {'hash': hash, 'text': pattern.text, 'hosts': pattern_details['hosts'], 'count': pattern_details['count'], 'data': data[:data_count], 'last_ts_delta': pattern.get_last_ts_delta(datetime.now())}
        else:
            pattern_details.update({'hash': hash})
            return pattern_details
