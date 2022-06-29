from preprocessing import preprocess, transform
from vect_model import vectorial_model
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity


docs = [
      'In computer science artificial intelligence sometimes called machine intelligence is intelligence demonstrated by machines',

      'Experimentation calculation and Observation is called science',

      'Physics is a natural science that involves the study of matter and its motion through space and time, along with related concepts such as energy and force',
      
      'In mathematics and computer science an algorithm is a finite sequence of well-defined computer-implementable instructions',

      'Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions',

      'Biochemistry is the branch of science that explores the chemical processes within and related to living organisms',

      'Sociology is the study of society, patterns of social relationships, social interaction, and culture that surrounds everyday life',
    
    ]
query = 'computer science'

def retrieval(docs,query):
    proc_docs = preprocess(docs)
    proc_query = preprocess([query])
    doc_vector,query_vector = transform(proc_docs,proc_query)
    print(query_vector)
    indexs = svd_model(doc_vector,query_vector)
    result = [proc_docs[i] for i in indexs]
    print(result)
    return result

def svd_model(doc_vector, query_vector):
    cosineSimilarities = cosine_similarity(doc_vector,query_vector).flatten()
    related_docs_indexs = cosineSimilarities.argsort()[:-10:-1]
    print(related_docs_indexs)
    return related_docs_indexs
    

retrieval(docs, query)