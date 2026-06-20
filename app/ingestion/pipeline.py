import os

from app.ingestion.pdf_reader import extract_text
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import create_embeddings

from app.vectordb.store_vectors import store_chunks

pdf_folder = "app/pdfs"

for file in os.listdir(pdf_folder):

    if file.endswith(".pdf"):

        path = os.path.join(
            pdf_folder,
            file
        )

        pages = extract_text(path)

        chunks = chunk_text(pages)

        embeddings = create_embeddings(chunks)

        store_chunks(
            chunks,
            embeddings
        )

        print(
            f"{file} processed."
        )
print(file)
print(len(chunks))