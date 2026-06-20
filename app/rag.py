from retrieval.retriever import search
from llm.gemini_client import ask_llm
from reranking.reranker import rerank


question = input("Ask: ")

results = search(question)
results = rerank(
    question,
    results
)

context = ""

sources = []

for result in results:

    context += (
        result.payload["text"]
        + "\n\n"
    )

    sources.append(

        (
            result.payload["file"],

            result.payload["page"]
        )
    )

answer = ask_llm(
    context,
    question
)

print(answer)

print()

print("Sources:")

for file, page in sources:

    print(
        f"{file} | Page {page}"
    )