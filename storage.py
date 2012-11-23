import os, codecs, sys
from datetime import datetime, timedelta
from tree import TPattern, Tree

DATA_PATH = os.path.realpath('./data')
TREE = Tree()

def get_hash(str):
	return hash(str) & sys.maxint

def load_patterns():
	loaded_patterns_hashes = {}
	pattern_path = os.path.join(DATA_PATH, "patterns")
	if os.path.exists(pattern_path):
		f = codecs.open(pattern_path, mode="r", encoding='utf-8')
		count = 0
		for line in f:
			if line.strip() != "":
				if count % 3 == 0:
					name = line.strip()
				if count % 3 == 1:
					logger = line.strip()
				if count % 3 == 2:
					pattern = line.strip()
					hash = get_hash("".join([name, logger, pattern]))
					if hash not in TREE.patterns:
						TREE.patterns.update({hash: TPattern(name, logger, pattern)})
						TREE.patterns_order.insert(0, hash)
					loaded_patterns_hashes.update({hash:name})
			count += 1
		f.close()
	if len(TREE.patterns) == 0:
		hash = get_hash("Default")
		TREE.patterns.update({hash: TPattern("Default", ".*", ".*")})
		TREE.patterns_order.insert(0, hash)
	for pattern_hash in TREE.patterns.keys():
		if pattern_hash not in loaded_patterns_hashes:
			latest_data = [item for item in TREE.patterns[pattern_hash].latest_data]
			del TREE.patterns[pattern_hash] 
			TREE.patterns_order.remove(pattern_hash)
			for item in latest_data:
				TREE.process_data_dict(item)

def load():

	load_patterns()
	raw_datapath = os.path.join(DATA_PATH, "raw")

	if os.path.exists(raw_datapath):
		data_files = os.listdir(raw_datapath)
		data_files.sort()
		for file in data_files:
			file_date = datetime.strptime(file, "%Y-%m-%d")
			if timedelta(days=2) + file_date < datetime.now():
				continue
			f = codecs.open(os.path.join(raw_datapath, file), mode="r", encoding='utf-8')
			data = ""
			for line in f:
				if line[:5] == "ERROR" or line[:5] == "INFO " or line[:5] == "WARN " or line[:5] == "FATAL":
					TREE.put(data)
					data = ""
				data += line
			TREE.put(data)
			f.close()
	else:
		os.makedirs(raw_datapath)

def reload_latest_data():
	load_patterns()
	defaultPattern = TREE.patterns[TREE.patterns_order[-1]]
	latest_data = [item for item in defaultPattern.latest_data]
	defaultPattern.latest_data.clear()
	for item in latest_data:
		defaultPattern.hosts[item['host']].remove(item)
		TREE.process_data_dict(item)

def put(data):
	date = TREE.put(data)
	date_file_path = os.path.join(os.path.join(DATA_PATH, "raw", date))
	f = codecs.open(date_file_path, mode="a", encoding='utf-8')
	f.write("%s\n" % data)
	f.close()

def get_raw_patterns():
	pattern_path = os.path.join(DATA_PATH, "patterns")
	if os.path.exists(pattern_path):
		f = codecs.open(pattern_path, mode="r", encoding='utf-8')
		data = f.read()
		f.close()
		return data.encode('utf-8')
	return ""

def save_patterns(data):
	pattern_path = os.path.join(DATA_PATH, "patterns")
	f = codecs.open(pattern_path, mode="w", encoding='utf-8')
	f.write(data.rstrip('\n').decode('utf8'))
	f.write(u'\n')
	f.close()
	reload_latest_data()

def add_pattern(name, logger, pattern):
        pattern_path = os.path.join(DATA_PATH, "patterns")
        f = codecs.open(pattern_path, mode="a", encoding='utf-8')
        f.write("# %s\n" % name)
        f.write("%s\n" % logger)
        f.write("%s\n" % pattern)
        f.close()
        reload_latest_data()
