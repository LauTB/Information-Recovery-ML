import numpy as np
import pandas as pd
import pyterrier as pt
from sklearn.ensemble import RandomForestRegressor
def start():
  if not pt.started():
    pt.init()
def get_dataset(name):
  return pt.datasets.get_dataset(name)

def get_index(dataset):
  index_path = "./index"
  indexer = pt.TRECCollectionIndexer(index_path, blocks=True)
  try:
    indexref = indexer.index(dataset.get_corpus())
    indexref.toString()
  except ValueError:
    indexref = dataset.get_index()
  index = pt.IndexFactory.of(indexref)
  return index

def get_topics_and_qrels(dataset):
  return (dataset.get_topics(),dataset.get_qrels())

def split_data(topics):
  return np.split(topics, [int(.6*len(topics)), int(.8*len(topics))])

def build_pipeline():
  pipeline = pt.FeaturesBatchRetrieve(index, wmodel="BM25", features=["WMODEL:Tf", "WMODEL:PL2"])
  rf = RandomForestRegressor(n_estimators=400)
  rf_pipe = pipeline >> pt.ltr.apply_learned_model(rf)
  return rf_pipe
def experiment(train_topics,test_topics,qrels):
  bm25 = pt.BatchRetrieve(index, wmodel="BM25")
  rf_pipe = build_pipeline()
  rf_pipe.fit(train_topics, qrels)
  r = pt.Experiment([bm25, rf_pipe], test_topics, qrels, ["map", "recall"], names=["BM25", "LTR"],save_dir="./")
  return r

start()
dataset = get_dataset("vaswani")
index = get_index(dataset)
topics, qrels = get_topics_and_qrels(dataset)
train_topics, valid_topics, test_topics = split_data(topics)
experiment(train_topics, test_topics,qrels)