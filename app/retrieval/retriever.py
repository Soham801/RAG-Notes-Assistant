from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = QdrantClient(
    host="localhost",
    port=6333
)

def search(query):

    query_vector = model.encode(query)

    results = client.query_points(
        collection_name="notes",
        query=query_vector.tolist(),
        limit=5
    )

    return results.points


results = search(
    "What is attention mechanism?"
)

for result in results:
    print()
    print(result.payload["text"])