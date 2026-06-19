from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)
vector = model.encode(chunk_text)   
{
 "chunk_id":1,
 "text":"...",
 "embedding":[...]
}