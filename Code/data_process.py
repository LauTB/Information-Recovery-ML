import ir_datasets
import json


def save_database(path, files, db):
    with open(f'{path}/{db}_db.json', 'w') as f:
        json.dump(files, f, indent=4)

def load_dataset(ds_name: str):
    ds = ir_datasets.load(ds_name)
    
    # guardando las queries
    queries = [q for q in ds.queries_iter()]
    q = [q_.text for q_ in queries[0:5]]
    with open(f"../{ds_name}_queries.txt", "w") as f:
        f.write("\n".join(q))
        f.close()

    return ds

def make_text_list(dataset):
    documents = []
    for doc in dataset.docs_iter():
        documents.append(doc.text)
    return documents

#if __name__ == "__main__":
#    d = load_dataset()
#    r = make_text_list(d)
#    print(r[0])