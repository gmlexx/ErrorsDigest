import re, uuid, sys
from datetime import datetime, timedelta
from host import THost
from pattern import TPattern

space_characters = [' ','\t','\n','\r']

class Tree:

    def __init__(self):
        self.patterns = {}
        self.patterns_rank = {}
        self.rank_counter = 0
        self.ranked_pattern_hashes = []
        self.metrics = {'processed': 0, 'checks': 0}

    def add_pattern(self, pattern):
        hash_value = hash(pattern.text) & sys.maxint
        if hash_value not in self.patterns:
            self.patterns.update({hash_value: pattern})
            self.patterns_rank.update({hash_value: 0})
            self.ranked_pattern_hashes.append(hash_value)
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
            checks = self.process_data_dict(data_dict)
            self.metrics['processed'] += 1
            self.metrics['checks'] += checks

        return datetime.now().date().strftime("%Y-%m-%d")

    def reset_ranks(self):
        self.ranked_pattern_hashes = sorted(self.patterns_rank, key=self.patterns_rank.get, reverse=True)
        for hash in self.ranked_pattern_hashes:
            self.patterns_rank[hash] = 0

    def process_data_dict(self, data_dict):
        for i, hash_value in enumerate(self.ranked_pattern_hashes):
            pattern = self.patterns[hash_value]
            if pattern.put(data_dict):
                self.patterns_rank[hash_value] += 1
                self.rank_counter += 1
                if self.rank_counter > 2000:
                    self.reset_ranks()
                    self.rank_counter = 0
                return i
        self.add_pattern(TPattern(data_dict))
        return len(self.ranked_pattern_hashes)

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
        digest.sort(key=lambda p: p['counts'][0]['delta'], reverse=True)
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
