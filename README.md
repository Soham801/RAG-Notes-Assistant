# 🚀 RAG Notes Assistant

> An AI-powered Retrieval-Augmented Generation (RAG) system that allows users to ask questions from their PDF documents using natural language.

Built using **FastAPI, Qdrant, Sentence Transformers, Gemini, and Streamlit**, this project demonstrates a production-inspired RAG pipeline with semantic search, reranking, conversational memory, and multi-document support.

---

## 📌 Features

✅ Multi-PDF Knowledge Base

✅ Semantic Search using Sentence Transformers

✅ Qdrant Vector Database

✅ FastAPI REST API

✅ Streamlit User Interface

✅ Gemini LLM Integration

✅ Source Citation Support

✅ Metadata Filtering

✅ Cross-Encoder Reranking

✅ Conversational Memory

---

# 🏗️ Architecture

```text
User Question
      │
      ▼
Embedding Generation
      │
      ▼
Qdrant Vector Search
      │
      ▼
Top 20 Retrieved Chunks
      │
      ▼
Cross Encoder Reranker
      │
      ▼
Top 5 Relevant Chunks
      │
      ▼
Conversation Memory
      │
      ▼
Gemini LLM
      │
      ▼
Final Answer + Sources
```

---

# 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| Vector Database | Qdrant |
| Embeddings | all-MiniLM-L6-v2 |
| Reranker | CrossEncoder |
| LLM | Google Gemini |
| PDF Parsing | PyPDF |
| API Testing | Swagger UI |

---

# 📂 Project Structure

```text
rag-notes-assistant/

├── app/
│
├── frontend/
│   └── app.py
│
├── ingestion/
│   ├── pdf_reader.py
│   ├── chunker.py
│   ├── embedder.py
│   └── pipeline.py
│
├── retrieval/
│   └── retriever.py
│
├── reranking/
│   └── reranker.py
│
├── memory/
│   └── memory.py
│
├── llm/
│   └── gemini_client.py
│
├── vectordb/
│   ├── create_collection.py
│   └── store_vectors.py
│
├── pdfs/
│
├── main.py
├── rag.py
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git https://github.com/Soham801/RAG-Notes-Assistant.git

cd rag-notes-assistant
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# 🐳 Start Qdrant

```bash
docker run -p 6333:6333 qdrant/qdrant
```

Qdrant Dashboard:

```text
http://localhost:6333/dashboard
```

---

# 📥 Add PDF Documents

Place your PDFs inside:

```text
app/pdfs/
```

Example:

```text
app/pdfs/

Attention-is-all-you-need.pdf
Deep-Learning.pdf
Operating-System.pdf
```

---

# 🧠 Generate Embeddings

```bash
python -m app.ingestion.pipeline
```

---

# 🚀 Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 💻 Start Streamlit Frontend

```bash
streamlit run app/frontend/app.py
```

Streamlit UI:

```text
http://localhost:8501
```

---

# 💬 Example Questions

- What is self-attention?
- Explain the Transformer architecture.
- What is backpropagation?
- What are convolutional neural networks?
- Compare RNN and Transformer.

---

# 🔍 Retrieval Pipeline

```text
Question
    ↓
Embedding Generation
    ↓
Vector Search
    ↓
Top 20 Chunks
    ↓
Reranking
    ↓
Best 5 Chunks
    ↓
Gemini
    ↓
Answer + Sources
```

---

# 📈 Advanced Features

### Multi-PDF Support

Query multiple documents simultaneously.

### Metadata Filtering

Search specific PDFs.

### CrossEncoder Reranking

Improves answer quality by selecting the most relevant chunks.

### Conversational Memory

Supports follow-up questions.

### Source Attribution

Returns the PDF name and page number.

---

# 🔮 Future Improvements

- Hybrid Search (BM25 + Vector Search)
- User Authentication
- PDF Upload UI
- Docker Deployment
- Cloud Deployment
- Chat History Database
- Agentic RAG Workflows

---

# 👨‍💻 Author

**Soham Deshmukh**

Computer Science Student | AI & GenAI Developer

### Skills

- Python
- FastAPI
- Generative AI
- Vector Databases
- Retrieval-Augmented Generation
- Large Language Models

---

# ⭐ Star the repository if you found it useful.