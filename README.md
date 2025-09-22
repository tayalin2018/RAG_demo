# RAG Demo (LangChain + FAISS + FastAPI)

**What this is**  
A tiny Retrieval-Augmented Generation service that indexes local `.txt` files with FAISS and answers questions via FastAPI.

**Results (local)**  
- Accuracy: avg F1 = **1.00**, contains = **6/6** (n=6)  
- Latency: ~ **1.0 s**/query  
- Example: Q “Which vector store does this demo use?” → A “The demo uses **FAISS** for vector search.”

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
