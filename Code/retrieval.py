from unittest import result
from .preprocessing import preprocess, transform
from .vect_model import vectorial_model
from .neural_network_model import neural_network_model
from .svd_retrieval import svd_model
from sklearn.feature_extraction.text import CountVectorizer
'''
docs = [
      'In computer science artificial intelligence sometimes called machine intelligence is intelligence demonstrated by machines',

      'Experimentation calculation and Observation is called science',

      'Physics is a natural science that involves the study of matter and its motion through space and time, along with related concepts such as energy and force',
      
      'In mathematics and computer science an algorithm is a finite sequence of well-defined computer-implementable instructions',

      'Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions',

      'Biochemistry is the branch of science that explores the chemical processes within and related to living organisms',

      'Sociology is the study of society, patterns of social relationships, social interaction, and culture that surrounds everyday life',
    
    ]
'''

docs = ['the computer science is la tiza',
        'Por mis cojones',
        'computer machine',
        'Biochemistry is the branch of science']

query = 'computer science'
query1 = 'computer'
query2 = 'my mom is computer scientific'
querys= [query,query1,query2]

def retrieval(docs, query, db, model, query_exp):
    proc_docs = preprocess(docs)
    proc_query = preprocess([query], query_exp)
    doc_vector,query_vector = transform(proc_docs,proc_query)
    indexs = None
    if model == 'v':
        # countVect = CountVectorizer()
        # doc_vector = countVect.fit_transform(proc_docs)
        # print(doc_vector.toarray())
        indexs = vectorial_model(doc_vector,query_vector)
    elif model == 'lsi':
        indexs = svd_model(doc_vector,query_vector)
    else:
        neural_network_model(proc_docs, proc_query,db)
    # print(indexs)
    result = [proc_docs[i] for i in indexs]
    return result

#retrieval(docs,query)

