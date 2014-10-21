import storage, cProfile

def load():
    count = storage.load()
    print 'Total patterns: ', len(storage.TREE.patterns)
    print 'Total messages: ', count

cProfile.run('load()')
