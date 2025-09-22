from fastapi import FastAPI
from pydantic import BaseModel
from chain import build_chain

chain = build_chain()
app = FastAPI(title="RAG Service")

class AskIn(BaseModel):
    question: str

class AskOut(BaseModel):
    answer: str

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/ask", response_model=AskOut)
def ask(inp: AskIn):
    answer = chain.invoke(inp.question)
    return AskOut(answer=answer)
