import os
from collections import defaultdict
from typing import List, Dict

folder_path_docs = 'C:/Users/hussein/Desktop/hw1_data/docs/'
folder_path_queries = 'C:/Users/hussein/Desktop/hw1_data/queries/'
file_list_docs = os.listdir(folder_path_docs)
file_list_queries = os.listdir(folder_path_queries)

documents = []
for file in file_list_docs:
    with open(os.path.join(folder_path_docs, file), 'r') as f:
        documents.append(f.read())

queries = []
for file in file_list_queries:
    with open(os.path.join(folder_path_queries, file), 'r') as f:
        queries.append(f.read())
print(queries[1])

#The code that extracts the vocabulary and creates the vector representation for each document and query.


def create_vectors(documents: List[str], queries: List[str]) -> Dict[str, List[int]]:
    term_freq = defaultdict(lambda: defaultdict(int))
    for doc in documents:
        for word in doc.split():
            term_freq[doc][word] += 1
    for query in queries:
        for word in query.split():
            term_freq[query][word] += 1
    vocabulary = set(word for doc in term_freq for word in term_freq[doc])
    vectors = {doc: [term_freq[doc][word] for word in vocabulary] for doc in term_freq}
    return vectors, vocabulary


vectors, vocabulary = create_vectors(documents,queries)
vectors