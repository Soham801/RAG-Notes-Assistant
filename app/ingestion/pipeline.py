from app.ingestion.pdf_reader import extract_text
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import create_embeddings

from app.vectordb.store_vectors import store_chunks

pdf_text = extract_text("app/pdfs/Attention-is-all-you-need.pdf")

chunks = chunk_text(pdf_text)

embeddings = create_embeddings(chunks)

store_chunks(
    chunks,
    embeddings
)