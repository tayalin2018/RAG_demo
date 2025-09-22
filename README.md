# GenAI Intern Starter — 3 tiny projects

This repo gives you three bite-sized, CV-ready projects aligned with *RAG* and *Agentic Automation with LLMs*, plus a minimal eval harness and observability bits.

## What’s inside

1. **01_rag_service/** — Retrieval-Augmented Generation microservice
   - LangChain (LCEL), FAISS vector store, FastAPI endpoint, Dockerfile
   - Ingestion script + Pydantic settings + simple tests
2. **02_agent_graph/** — Agentic workflow with tools
   - LangGraph loop (agent → tools → agent), FastAPI endpoint, Dockerfile
3. **03_eval_and_obs/** — Quick evaluation + logging
   - JSONL eval set + lexical F1 + contains metric; structured JSON logs

## Quick start (local)

Create a virtualenv, then for each project:

```bash
cd 01_rag_service
cp .env.example .env  # add your API key(s) if using remote models
pip install -r requirements.txt
python ingest.py           # builds FAISS index from data/sample_docs
uvicorn app:app --reload   # http://127.0.0.1:8000/docs
```

For agent:

```bash
cd 02_agent_graph
cp .env.example .env
pip install -r requirements.txt
uvicorn app:app --reload   # http://127.0.0.1:8001/docs
```

For eval:

```bash
cd 03_eval_and_obs
pip install -r requirements.txt
python eval.py --service-url http://127.0.0.1:8000/ask --dataset eval/data.jsonl
```

## Docker (optional)

Each service has a `Dockerfile`. Example:

```bash
cd 01_rag_service
docker build -t rag-service:dev .
docker run -p 8000:8000 --env-file .env rag-service:dev
```

## Notes

- These are minimal educational skeletons. Swap models/providers (OpenAI, Azure, Anthropic, local via Ollama) as you like.
- The RAG service saves a FAISS index locally to `index/`.
- The agent project includes two tools: a safe calculator and a toy “lookup” over a local text file.
- Keep commits small and add a concise README badge-like section to your CV.
