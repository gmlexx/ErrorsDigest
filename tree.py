import re, uuid, sys
from collections import deque
from datetime import datetime, timedelta

space_characters = [' ','\t','\n','\r']


class THost:

    def __init__(self, name):
        self.name = name
        self.errors = {}
        self.latest_data = deque(maxlen = 10)

    def put(self, data_dict):
        find = False
        ts = data_dict['ts']
        data_dict['message_lines'] = data_dict['message'].split('\r\n')
        for timestamp in self.errors.keys():
            if (ts - timestamp).seconds < 60:
                self.errors[timestamp] += 1
                find = True
            if timestamp < datetime.now() - timedelta(hours=48):
                del self.errors[timestamp]
        if find == False:
            self.errors.update({data_dict['ts']: 1})
        self.latest_data.append(data_dict)

    def remove(self, data_dict):
        ts = data_dict['ts']
        items_to_remove = []
        for item in self.latest_data:
            if item['id'] == data_dict['id']:
                items_to_remove.append(item)
                for timestamp in self.errors.keys():
                    if (ts - timestamp).seconds < 60:
                        self.errors[timestamp] -= 1
        for item in items_to_remove:
            self.latest_data.remove(item)

    def get_count(self, td):
        count = 0
        for ts in self.errors.keys():
            if ts > td:
                count += self.errors[ts]
        return count

class TPattern:

    def __init__(self, name, logger, pattern, default = False):
        self.logger = logger
        self.pattern = pattern
        self.name = name
        self.logger_re = re.compile(logger, re.DOTALL)
        self.pattern_re = re.compile(pattern, re.DOTALL)
        self.hosts = {}
        self.latest_data = deque(maxlen = 10)
        self.last_ts = None
        self.default = default

    def put(self, data_dict):
        logger = data_dict['logger']
        message = data_dict['message']
        host = data_dict['host']
        if self.default or self.logger_re.match(logger) != None:
            if self.default or self.pattern_re.match(message) != None:
                self.latest_data.append(data_dict)
                if host not in self.hosts:
                    self.hosts.update({host: THost(host)})
                self.hosts[host].put(data_dict)
                self.last_ts = data_dict['ts']
                return True
        return False

    def get_data(self, host, td):
        if host not in self.hosts:
            return []
        data = [ item for item in self.hosts[host].latest_data if item['ts'] > td ]
        data.reverse()
        return data

    def get_counts(self, time_deltas):
        counts = []
        total = 0
        for min in time_deltas:
            td = datetime.now() - timedelta(minutes=min)
            count = 0
            for host in self.hosts.keys():
                count += self.hosts[host].get_count(td)
                total += count
            counts.append({'min': min, 'count': count})
        return (counts, total)

    def get_details(self, td):
        details = {'name': self.name, 'count': 0, 'hosts': []}
        for host in self.hosts.keys():
            host_count = self.hosts[host].get_count(td)
            if host_count > 0:
                details['hosts'].append({'name': host, 'count': self.hosts[host].get_count(td)})
                details['count'] += host_count
        return details

    def get_last_ts_delta(self, now):
        if not self.last_ts:
            return ""
        delta = timedelta(0) if now < self.last_ts else now - self.last_ts
        str_result = "%s days %s hours %s min" % (delta.days, int(delta.seconds/3600), int(delta.seconds%3600/60))
        return str_result.replace('0 days ','').replace('0 hours ','')

class Tree:

    def __init__(self):
        self.patterns = {}
        self.patterns_order = []
        self.patterns_rank = {}
        self.rank_counter = 0
        self.ranked_patterns = None
        self.default_pattern = None

    def add_pattern(self, pattern):
        hash_value = hash("".join([pattern.name, pattern.logger, pattern.pattern])) & sys.maxint
        self.patterns.update({hash_value: pattern})
        if not pattern.default:
            self.patterns_rank.update({hash_value: 0})
            self.patterns_order.insert(0, hash_value)
        else:
            self.patterns_order.append(hash_value)
            self.default_pattern = pattern
        return hash_value

    def get_ranked_patterns(self):
        if not self.ranked_patterns:
            self.ranked_patterns = sorted(self.patterns_rank, key=self.patterns_rank.get, reverse = True)
            self.rank_counter = 0
        return self.ranked_patterns

    def clear(self):
        self.patterns = {}
        self.patterns_order = []
        self.rank_counter = 0
        self.ranked_patterns = None

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
                if parts_count == 6:
                    break
            else:
                word.append(c)

        parts.append(data[c_count:])

        if len(parts) > 5:
            level = parts[0]
            host = parts[4]
            logger = parts[5]
            message = " ".join((parts[6:]))
            ts = datetime.strptime("%s %s" % (parts[1], parts[2]), "%Y-%m-%d %H:%M:%S,%f")
            ts_string = "".join([parts[1], " ", parts[2]])
            data_dict = {'level':level, 'host':host, 'logger':logger, 'message':message, 'ts':ts, 'id': uuid.uuid4(), 'ts_string':ts_string}
            self.process_data_dict(data_dict)

        return datetime.now().date().strftime("%Y-%m-%d")

    def process_data_dict(self, data_dict):
        for hash_value in self.get_ranked_patterns():
            pattern = self.patterns[hash_value]
            if pattern.put(data_dict):
                self.patterns_rank[hash_value] += 1
                self.rank_counter += 1
                if self.rank_counter > 1000:
                    self.ranked_patterns = None
                return
        self.default_pattern.put(data_dict)

    def get_digest(self, time_deltas):
        digest = []
        now = datetime.now()
        for hash in self.patterns_order:
            pattern = self.patterns[hash]
            counts, total = pattern.get_counts(time_deltas)
            digest.append({'name': pattern.name, 'total': total, 'counts': counts, 'hash': hash, 'is_default': (pattern.name.lower().replace(' ','') == '#default'), 'last_ts_delta': pattern.get_last_ts_delta(now)})
        return {'digest':digest}

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
            return {'hash': hash, 'name': pattern.name, 'hosts': pattern_details['hosts'], 'count': pattern_details['count'], 'data': data[:data_count], 'last_ts_delta': pattern.get_last_ts_delta(datetime.now())}
        else:
            pattern_details.update({'hash': hash})
            return pattern_details

