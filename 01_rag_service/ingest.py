import os
from pathlib import Path
from config import settings

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def build_index():
    data_dir = Path(settings.data_dir)
    if not data_dir.exists():
        raise FileNotFoundError(f"Data dir not found: {data_dir}")

    loader = DirectoryLoader(str(data_dir), glob="**/*.txt", loader_cls=TextLoader, show_progress=True)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        add_start_index=True,
    )
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(model=settings.embed_model, api_key=settings.openai_api_key)
    vs = FAISS.from_documents(chunks, embeddings)
    os.makedirs(os.path.dirname(settings.index_path), exist_ok=True)
    vs.save_local(settings.index_path)
    print(f"Saved FAISS index to {settings.index_path}; chunks={len(chunks)}")

if __name__ == "__main__":
    build_index()
