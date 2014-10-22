import os, codecs
from datetime import datetime, timedelta
from tree import Tree
from progressbar import ProgressBar, Bar, Percentage, FileTransferSpeed

DATA_PATH = os.path.realpath('./data')
TREE = Tree()

def load():

    raw_datapath = os.path.join(DATA_PATH, "raw")
    count = 0

    if os.path.exists(raw_datapath):
        data_files = os.listdir(raw_datapath)
        data_files.sort()
        for file in data_files:
            filename = os.path.join(raw_datapath, file)
            with codecs.open(filename, mode="r", encoding='utf-8') as f:
                data = ""
                total_size = os.path.getsize(filename)
                if total_size == 0:
                    continue
                pbar = ProgressBar(widgets=['Loading %s: ' % file, Percentage(), Bar(), FileTransferSpeed()], maxval=total_size).start()
                for line in f:
                    if line[:5] == "WARN " or line[:5] == "ERROR" or line[:5] == "INFO " or line[:5] == "DEBUG" or line[:5] == "FATAL":
                        count += 1
                        TREE.put(data)
                        data = ""
                    data += line
                    pbar.update(f.tell())
                pbar.finish()
                TREE.put(data)
                count += 1
    else:
        os.makedirs(raw_datapath)
    return count

def put(data):
    d = data.replace('\r\n', '\n')
    date = TREE.put(d)
    date_file_path = os.path.join(os.path.join(DATA_PATH, "raw", date))
    f = codecs.open(date_file_path, mode="a", encoding='utf-8')
    f.write("%s\n" % d)
    f.close()
