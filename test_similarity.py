# coding: utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = {1:'Diadoc.FilterIndex.Impl.LiveIndexReading.LiveIndexTaskReadQueueWorker Diadoc.FilterByBillingTimestampIndexHost Will retry request to LiveIndex (null)',
             2:'Diadoc.FilterIndex.Impl.LiveIndexReading.LiveIndexTaskReadQueueWorker Diadoc.FilterByPacketIdIndexHost Will retry request to LiveIndex (null)'}

tfidf_vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b[a-zA-Z_]+\b')
tfidf_matrix = tfidf_vectorizer.fit(documents.values())

vectors = tfidf_matrix.transform(['Diadoc.FilterIndex.Impl.LiveIndexReading.LiveIndexTaskReadQueueWorker Diadoc.FilterByBillingTimestampIndexHost Will retry request to LiveIndex (null)'])

for s in cosine_similarity(tfidf_matrix.transform(documents.values()), vectors):
    print s[0]
