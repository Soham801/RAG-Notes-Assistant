from retrieval.retriever import search
from llm.gemini_client import ask_llm

question = input("Ask: ")

results = search(question)

context = ""

for result in results:
    context += result.payload["text"]
    context += "\n\n"

answer = ask_llm(
    context,
    question
)

print(answer)