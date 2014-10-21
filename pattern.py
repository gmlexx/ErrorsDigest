from collections import deque
from host import THost
from datetime import datetime, timedelta

class TPattern:

    def __init__(self, data_dict):
        self.text = data_dict['text']
        self.message_lines = data_dict['message_lines']
        self.hosts = {}
        self.latest_data = deque(maxlen = 10)
        self.last_ts = None

    def put(self, data_dict):
        text = data_dict['text']
        host = data_dict['host']
        self.latest_data.append(data_dict)
        if host not in self.hosts:
            self.hosts.update({host: THost(host)})
        self.hosts[host].put(data_dict)
        self.last_ts = data_dict['ts']

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
        details = {'message_lines': self.message_lines, 'count': 0, 'hosts': []}
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
