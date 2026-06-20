from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = QdrantClient(
    host="localhost",
    port=6333
)

def search(
    query,
    file_name=None
):

    query_vector = model.encode(query)

    if file_name:

        results = client.query_points(

            collection_name="notes",

            query=query_vector.tolist(),

            limit=20,

            query_filter=Filter(
                must=[
                    FieldCondition(
                        key="file",
                        match=MatchValue(
                            value=file_name
                        )
                    )
                ]
            )
        )

    else:

        results = client.query_points(

            collection_name="notes",

            query=query_vector.tolist(),

            limit=20
        )

    return results.points


results = search(
    "What is attention?",
    "Attention-is-all-you-need.pdf"
)

for result in results:

    print()

    print(
        result.payload["file"]
    )

    print(
        result.payload["page"]
    )

    print(
        result.payload["text"][:200]
    )