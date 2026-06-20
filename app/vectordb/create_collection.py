from qdrant_client.models import Distance, VectorParams
from qdrant_client import QdrantClient

client = QdrantClient(
    host="localhost",
    port=6333
)

client.create_collection(
    collection_name="notes",

    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

print("Collection created.")