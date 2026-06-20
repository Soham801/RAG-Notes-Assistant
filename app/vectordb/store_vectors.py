from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

client = QdrantClient(
    host="localhost",
    port=6333
)

def store_chunks(chunks, embeddings):

    points = []

    for i in range(len(chunks)):

        points.append(
            PointStruct(
                id=i,

                vector=embeddings[i].tolist(),

                payload={
                    "text": chunks[i]
                }
            )
        )

    client.upsert(
        collection_name="notes",
        points=points
    )

    print("Vectors stored.")