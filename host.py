from collections import deque
from datetime import datetime, timedelta

class THost:

    def __init__(self, name):
        self.name = name
        self.errors = {}
        self.latest_data = deque(maxlen = 10)

    def put(self, data_dict):
        find = False
        ts = data_dict['ts']
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
