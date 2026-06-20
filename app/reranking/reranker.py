from sentence_transformers import CrossEncoder

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(
    question,
    results
):

    pairs = []

    for result in results:

        pairs.append(

            (
                question,

                result.payload["text"]
            )
        )

    scores = reranker.predict(
        pairs
    )

    ranked = sorted(

        zip(
            scores,
            results
        ),

        reverse=True,

        key=lambda x: x[0]
    )

    return [

        result

        for score,
        result

        in ranked[:5]
    ]