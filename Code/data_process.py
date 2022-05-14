import ir_datasets

def load_dataset():
    return ir_datasets.load("vaswani")

def make_text_list(dataset):
    documents = []
    for doc in dataset.docs_iter():
        documents.append(doc.text)
    return documents

if __name__ == "__main__":
    d = load_dataset()
    r = make_text_list(d)
    print(r[0])