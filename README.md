# RAG Demo (LangChain + FAISS + FastAPI)

**What this is**  
A tiny Retrieval-Augmented Generation service that indexes local `.txt` files with FAISS and answers questions via FastAPI.

### Demo results (RAG microservice)

- **Data:** `data/sample_docs` (6 questions)  
- **Model:** as set in `.env` (default: `gpt-4o-mini`)  
- **Retriever k:** 4 · **Chunk size/overlap:** 500 / 100

**Summary:** 6/6 correct · Contains rate **100%** · Avg F1 **1.00** · Avg latency **2.22 s** (n=6)

| Question | Answer (short) | F1 | Contains | Latency |
|---|---|---:|:---:|---:|
| What does RAG stand for? | Retrieval-Augmented Generation. | 1.00 | 1 | 2.88 s |
| Which vector store does this demo use? | FAISS. | 1.00 | 1 | 2.12 s |
| Which framework powers the web API? | FastAPI. | 1.00 | 1 | 1.74 s |
| Which endpoints does the service expose? | GET `/healthz`, POST `/ask`. | 1.00 | 1 | 1.93 s |
| How many results does the retriever return by default? | 4. | 1.00 | 1 | 2.23 s |
| What chunk size and overlap are configured? | 500 / 100. | 1.00 | 1 | 2.39 s |

**Extra Q&A**

- **Q:** What does Schwarz IT focus on?  
  **A:** RAG (Retrieval-Augmented Generation) and agentic automation.

**How it works (RAG in 3 steps)**  
1) Ingest chunks + embeddings → 2) FAISS index → 3) Retrieve + LLM answer  
Endpoints: `GET /healthz`, `POST /ask` with `{ "question": "..." }`.

**Run locally:**  
`cd 01_rag_service && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && cp .env.example .env && python ingest.py && uvicorn app:app --reload`
> Requires an OpenAI API key in `.env`.  

## Quick Start 
1) `cd 01_rag_service && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
2) `cp .env.example .env`  → put your `OPENAI_API_KEY=...` in `.env`
3) `python ingest.py && uvicorn app:app --reload`

### Tech stack & endpoints
- **Stack:** LangChain · FAISS · FastAPI · Pydantic
- **Endpoints:** `GET /healthz` · `POST /ask` (JSON: `{ "question": "..." }`)

### 10-second test (curl)
```bash
curl http://127.0.0.1:8000/healthz
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"Which vector store does this demo use?"}'
```
