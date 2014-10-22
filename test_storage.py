import storage

count = storage.load()
print 'Total patterns: ', len(storage.TREE.patterns)
print 'Total messages: ', count

