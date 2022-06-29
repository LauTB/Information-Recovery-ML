from sre_constants import BIGCHARSET
from traceback import print_tb
import keras as k
from keras import layers as kl
from keras import  models as km
from .corpus_preparation import corpus_preparation
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

def neural_network_model(doc_vector,query_vector,ds_name):#,q_similarity):
    #preparar el corpus
    q, ranked_results,term_doc = corpus_preparation(ds_name)
    #print("q[0]",len(q[0]))
    #print(model.get_weights())
    print("cant de docs",len(doc_vector))
    count_docs = len(doc_vector)#doc_vector.get_shape()[0]
    count_terms_docs = len(q[0])#doc_vector.get_shape()[1]
    #count_terms_q = query_vector.nnz
    
    #definir las capas y crear el modelo
    terms_doc_layer = kl.Dense(units=count_terms_docs,input_shape=[count_terms_docs])
    output_doc_layer = kl.Dense(units=count_docs)
    model = km.Sequential([terms_doc_layer,output_doc_layer])

    #modificar los pesosy los sesgos
    #bias_term_doc = [0 for _ in range(terms_doc_layer.units)]
    #print("q[0]",q[0])
    #print(terms_doc_layer.get_weights.shape())
    #terms_doc_layer.set_weights([q[0],bias_term_doc])
    
    #bias_doc = [0 for _ in range(output_doc_layer.units)]
    #terms_doc_layer.set_weights([doc_vector.toarray(),bias_doc])

    #print(model.get_weights())

    model.compile(
        optimizer = k.optimizers.Adam(0.1),
        loss = 'mean_squared_error',
        sample_weight_mode="temporal" 
    )
    
    print("q",len(q),len(q[0]))
    print("rr",len(ranked_results),len(ranked_results[0]))
    #print(ranked_results[0])
    X_train,y_train,X_test,y_test = train_test_split(q,ranked_results)#,test_size=0.6,random_state=40)
    print("x",len(X_train))
    print("y",len(y_train))

    hist = model.fit(X_train,y_train,epochs = 10,verbose=False)
    #model.fit_generator(generator(), epochs=10)
    
    plt.xlabel("Epoca")
    plt.ylabel("Magnitud de perdida")
    plt.plot(hist.history["loss"])
    #print("capas del modelo", model.layers)
    return

def generator(X_train,y_train,q, ranked_result,model):
    while 1:
        for i in range(len(X_train)):
            bias_term_doc = [0 for _ in range(len(X_train[i]))]
            model.set_weights([X_train[i],bias_term_doc])
            yield (X_train[i], y_train[i])

    
 
