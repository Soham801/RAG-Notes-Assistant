from fastapi import FastAPI
from pydantic import BaseModel

from app.retrieval.retriever import search
from app.llm.gemini_client import ask_llm

app = FastAPI()

class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "RAG API Running"
    }


@app.post("/ask")
def ask(query: Query):

    results = search(query.question)

    context = ""

    for result in results:
        context += result.payload["text"]
        context += "\n\n"

    answer = ask_llm(
        context,
        query.question
    )

    return {
        "answer": answer
    }