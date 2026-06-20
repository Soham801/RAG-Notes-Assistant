def chunk_text(
    pages,
    chunk_size=500,
    overlap=100
):

    chunks = []

    chunk_id = 0

    for page in pages:

        start = 0

        while start < len(page["text"]):

            end = start + chunk_size

            chunks.append({

                "chunk_id": chunk_id,

                "text":
                page["text"][start:end],

                "page":
                page["page"],

                "file":
                page["file"]
            })

            chunk_id += 1

            start += (
                chunk_size - overlap
            )

    return chunks