import glob 
import codecs
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
#import pandas as pd
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(docs):
    
    proc_docs =  []
    for doc in docs:
        #get_tokens
        tokens = nltk.word_tokenize(doc)
        #removing stopwords
        new_doc = remove_stopwords(tokens)
        new_doc = query_expansion(new_doc)
        #stemming
        ps = PorterStemmer()
        stemmed = []
        for word in new_doc:
            stemmed.append(ps.stem(word))
        proc_docs.append(' '.join(stemmed))
    return proc_docs


def remove_stopwords(doc):
    cleaned_text = []
    stop_words = set(stopwords.words('english'))
    for word in doc:
        if word not in stop_words:
            cleaned_text.append(word)
    return cleaned_text

def transform(proc_docs,query):
    vectorizerX = TfidfVectorizer()
    vectorizerX.fit(proc_docs)

    doc_vector = vectorizerX.transform(proc_docs)
    query_vector = vectorizerX.transform(query)

    return doc_vector,query_vector


def query_expansion(query):
    synonyms = []
    holonyms = []
    meronyms = []

    for word in query:
        for syn in wordnet.synsets(word):
            for i in syn.lemmas():
                synonyms.append(i.name())
        for items in wordnet.synsets(word):
            for lm in items.part_holonyms():
                holonyms += lm.lemma_names()
            for lm in items.part_meronyms():
                meronyms += lm.lemma_names()
                
    result = synonyms + holonyms + meronyms
    return list(set(result))
