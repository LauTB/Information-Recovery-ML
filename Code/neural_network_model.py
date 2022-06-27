from sre_constants import BIGCHARSET
from traceback import print_tb
import keras as k
from keras import layers as kl
from keras import  models as km
from .corpus_preparation import corpus_preparation
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

def neural_network_model(doc_vector,query_vector,ds_name):#,q_similarity):
    proc_vector= doc_vector
    countVect = CountVectorizer()
    doc_vector = countVect.fit_transform(proc_vector)
    print(doc_vector)

    count_docs = len(proc_vector)#doc_vector.get_shape()[0]
    count_terms_docs = len(doc_vector)#doc_vector.get_shape()[1]
    count_terms_q = query_vector.nnz
    
    #definir las capas y crear el modelo
    terms_doc_layer = kl.Dense(units=count_terms_docs,input_shape=[count_terms_docs])
    output_doc_layer = kl.Dense(count_docs)
    model = km.Sequential([terms_doc_layer,output_doc_layer])

    #preparar el corpus
    q, ranked_results = corpus_preparation(ds_name)
    print("q[0]",len(q[0]))
    print(model.get_weights())

    #modificar los pesosy los sesgos
    bias_term_doc = [0 for _ in range(terms_doc_layer.units)]
    #bias_doc = [0 for _ in range(output_doc_layer.units)]
    terms_doc_layer.set_weights([q[0],bias_term_doc])
    #terms_doc_layer.set_weights([,bias_doc])

    print(model.get_weights())

    model.compile(
        optimizer = k.optimizers.Adam(0.1),
        loss = 'mean_squared_error'
    )
    
    Q_train, rr_train = train_test_split(q,ranked_results,test_size=0.5,random_state=40)
    print(Q_train)

    model.fit(Q_train,rr_train,epochs = 1000,verbose=False)

    
    #print("capas del modelo", model.layers)
    return

def build_weight_matrix_l1_l2(doc_vector,query_vector):
    
    return

def build_weight_matrix_l2_l3(doc_vector,query_vector):
    return