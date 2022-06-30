from sklearn.metrics.pairwise import cosine_similarity

def vectorial_model(doc_vector,query_vector):
    cosineSimilarities = cosine_similarity(doc_vector,query_vector).flatten()
    # print(cosineSimilarities)
    related_docs_indexs = cosineSimilarities.argsort()[:-10:-1]
    # print(related_docs_indexs)
    return related_docs_indexs
    