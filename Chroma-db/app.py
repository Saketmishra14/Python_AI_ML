import chromadb
chroma_client = chromadb.Client()

from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

default_ef = DefaultEmbeddingFunction()

collection_name="test_collection"

collection=chroma_client.get_or_create_collection(collection_name,embedding_function=default_ef)

documents=[
    {"id":"doc1","text":"Hello,World"},
    {"id":"doc2","text":"Hello, How Are You Today?"},
    {"id":"doc3","text":"Good, Bye See You Later."}
]

for doc in documents:
    collection.upsert(ids=doc["id"],documents=doc["text"])


# define a query text
query_text="hello, world!"

results=collection.query(
    query_texts=[query_text],
    n_results=3
)

for idx, document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]
    print(
        f" For the query: {query_text}, \n Found similar document: {document} (ID: {doc_id}, Distance: {distance})"
    )

