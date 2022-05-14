
# Import Section
from sklearn.feature_extraction.text import TfidfVectorizer

# Data Section

def get_corpus():
    return [] 

corpus = [i for i in get_corpus()]


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_names())
#['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
# print(X.shape)