import os, codecs
from datetime import datetime, timedelta
from tree import TPattern, Tree
from progressbar import ProgressBar, Bar, Percentage, FileTransferSpeed

DATA_PATH = os.path.realpath('./data')
TREE = Tree()

def load_patterns():
    loaded_patterns_hashes = {}
    pattern_path = os.path.join(DATA_PATH, "patterns")
    if os.path.exists(pattern_path):
        with codecs.open(pattern_path, mode="r", encoding='utf-8') as f:
            count = 0
            for line in f:
                if line.strip() != "":
                    if count % 3 == 0:
                        name = line.strip()
                    if count % 3 == 1:
                        logger = line.strip()
                    if count % 3 == 2:
                        pattern = line.strip()
                        hash_value = TREE.add_pattern(TPattern(name, logger, pattern))
                        loaded_patterns_hashes[hash_value] = None
                    count += 1
    hash_value = TREE.add_pattern(TPattern("Default", ".*", ".*", default = True))
    loaded_patterns_hashes[hash_value] = None
    for pattern_hash in TREE.patterns.keys():
        if pattern_hash not in loaded_patterns_hashes:
            latest_data = [item for item in TREE.patterns[pattern_hash].latest_data]
            print "Remove pattern %s" % TREE.patterns[pattern_hash].name.encode('utf-8')
            del TREE.patterns[pattern_hash]
            del TREE.patterns_rank[pattern_hash]
            TREE.patterns_order.remove(pattern_hash)
            for item in latest_data:
                TREE.process_data_dict(item)
    TREE.ranked_patterns = []

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
            filename = os.path.join(raw_datapath, file)
            with codecs.open(filename, mode="r", encoding='utf-8') as f:
                data = ""
                total_size = os.path.getsize(filename)
                if total_size == 0:
                    continue
                pbar = ProgressBar(widgets=['Loading %s: ' % file, Percentage(), Bar(), FileTransferSpeed()], maxval=total_size).start()
                for line in f:
                    if line[:5] == "ERROR" or line[:5] == "INFO " or line[:5] == "WARN " or line[:5] == "FATAL":
                        TREE.put(data)
                        data = ""
                    data += line
                    pbar.update(f.tell())
                pbar.finish()
                TREE.put(data)
    else:
        os.makedirs(raw_datapath)

def reload_latest_data():
    load_patterns()
    defaultPattern = TREE.default_pattern
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
        with codecs.open(pattern_path, mode="r", encoding='utf-8') as f:
            data = f.read()
            return data.encode('utf-8')
    return ""

def save_patterns(data):
    pattern_path = os.path.join(DATA_PATH, "patterns")
    with codecs.open(pattern_path, mode="w", encoding='utf-8') as f:
        f.write(data.rstrip('\n').decode('utf8'))
        f.write(u'\n')
    reload_latest_data()

def add_pattern(name, logger, pattern):
    pattern_path = os.path.join(DATA_PATH, "patterns")
    with codecs.open(pattern_path, mode="a", encoding='utf-8') as f:
        f.write("# %s\n" % name)
        f.write("%s\n" % logger)
        f.write("%s\n" % pattern)
    reload_latest_data()
