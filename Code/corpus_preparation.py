import ir_datasets

def get_words(dataset):
#construir el diccionario de términos-indice
  words = {}
  index = 0
  for doc in dataset.docs_iter():
      text = doc.text.split()
      for t in text:
        t = t.lower()
        try:
          a = words[t]
        except KeyError:
          words[t] = index
          index += 1
  return words

def create_queries_vec(dataset, words):
  #crear vector de queries
  queries = []
  for query in dataset.queries_iter():
    query_format = [0 for _ in range(len(words))]
    title = query.text.split()[:-1]
    for t in title:
      t = t.lower()
      try:
        index= words[t]
        query_format[index]=1
      except Exception as e:
        continue
        #print("Warning: the term " + t + " does not belong to the vocabulary and will be ignored")
    queries.append(query_format)
  return queries

def create_doc_vec(dataset):
  #crear vector de documentos
  docs = dataset.docs_count()
  doc_index = 0
  docs_ids = {}
  for doc in dataset.docs_iter():
    id = doc.doc_id
    try:
      docs_ids[id].append(id)    
    except KeyError:
      docs_ids[id] = [doc_index]
      doc_index += 1
  return docs_ids

def get_all_relevance_from_query(dataset, qid):
  data = []
  for q in dataset.qrels_iter():
    if str(q.query_id) == str(qid):
      data.append((q.doc_id, q.relevance))
  return data

def load_ranking(dataset, query):
  doc = [0 for _ in range(dataset.docs_count())]
  for d, r in query:
    d = int(d) -1
    if r == 4:
      doc[d] = 0.9#super relevant
    elif r == 3:
      doc[d] = 0.75 #relevant
    elif r == 2:
      doc[d] = 0.6 #kind of relevant
    else:
      doc[d] = 0.4 #r==1 and not really relevant
  return doc


def corpus_preparation(ds_name):
  dataset = ir_datasets.load(ds_name)
  words = get_words(dataset)
  q = create_queries_vec(dataset, words)
  ranked_results = []
  for index, query in enumerate(q):
      ranked = get_all_relevance_from_query(dataset, index+1)
      vector = load_ranking(dataset, ranked)
      ranked_results.append(vector)
  return q,ranked_results

'''
  if __name__ == "__main__":
        dataset = ir_datasets.load("cranfield")
    words = get_words(dataset)
    q = create_queries_vec(dataset, words)
    ranked_results = []
    for index, query in enumerate(q):
        ranked = get_all_relevance_from_query(dataset, index+1)
        vector = load_ranking(dataset, ranked)
        ranked_results.append(vector)
    print('en q están las queries como binarios y en ranked result para cada query los documentod relevantes')
'''