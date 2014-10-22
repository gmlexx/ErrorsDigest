# coding: utf-8
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = ["""

        DiadocCommons.Focus.FocusClient Diadoc.CounteragentsDomainHost No orgs with INN 0276130381 and KPP  found in Focus RequestId: 5d0a9bc3-1ae3-4d8c-9836-558365677c2f, Thumbprint: 20f2cd524c145ce3cda5c4da832a1764a9100595, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

        9b9c7b1f-3225-4f05-b559-cdeda5f94c4e

        20f2cd524c145ce3cda5c4da832a1764a9100595

        635495736365885631

        0

        1F7B9C9B2532054FB559CDEDA5F94C4EC196866B340AB14F8C2A08238DCC0E9D, UserId: 9b9c7b1f-3225-4f05-b559-cdeda5f94c4e

"""]

tfidf_vectorizer = CountVectorizer(token_pattern=r'(?u)\b[a-zA-Z_\':,]+[\s(){}\[\]=.]', lowercase=False)
similarities = []

tfidf_matrix = tfidf_vectorizer.fit(documents)

vectors = tfidf_matrix.transform(["""Diadoc.Kanso DC.Google.Handlers [KansoWrite-169800000559] AsyncUdpClient. Receive timeout. EndPoint: 192.168.52.253:53. Timeout: 00:00:00.5000000 (null)"""])

similarities = cosine_similarity(tfidf_matrix.transform(documents), vectors)
print "Maximum: %s" % max([s[0] for s in similarities])

#print tfidf_matrix.inverse_transform(tfidf_matrix.transform(documents))
#print tfidf_matrix.inverse_transform(vectors)
