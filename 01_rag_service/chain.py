from typing import Dict, Any
from config import settings

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

SYSTEM_PROMPT = "You are a helpful assistant. Use the provided context to answer. If unsure, say you don't know."

def _load_retriever():
    embeddings = OpenAIEmbeddings(model=settings.embed_model, api_key=settings.openai_api_key)
    vs = FAISS.load_local(settings.index_path, embeddings, allow_dangerous_deserialization=True)
    return vs.as_retriever(search_kwargs={"k": settings.k})

def _format_docs(docs):
    return "\n\n".join([f"[{i}] {d.page_content}" for i, d in enumerate(docs, 1)])

def build_chain():
    retriever = _load_retriever()
    llm = ChatOpenAI(model=settings.model_name, temperature=0, api_key=settings.openai_api_key)

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "Question: {question}\n\nContext:\n{context}\n\nAnswer concisely.")
    ])

    # LCEL: prepare inputs in parallel
    setup = RunnableParallel({
        "context": retriever | _format_docs,
        "question": RunnablePassthrough()
    })

    chain = setup | prompt | llm | StrOutputParser()
    return chain
