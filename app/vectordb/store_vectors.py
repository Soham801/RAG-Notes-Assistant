from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

client = QdrantClient(
    host="localhost",
    port=6333,
    timeout=120
)


def store_chunks(chunks, embeddings):

    points = []

    for i in range(len(chunks)):

        points.append(

            PointStruct(
                id=i,

                vector=embeddings[i].tolist(),

                payload={
                    "text": chunks[i]["text"],
                    "page": chunks[i]["page"],
                    "file": chunks[i]["file"]
                }
            )
        )

    batch_size = 100

    for i in range(0, len(points), batch_size):

        batch = points[i:i + batch_size]

        client.upsert(
            collection_name="notes",
            points=batch
        )

        print(
            f"Stored batch {i//batch_size + 1}"
        )

    print("Vectors stored.")