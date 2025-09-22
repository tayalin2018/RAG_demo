from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Model + embeddings
    model_name: str = Field(default="gpt-4o-mini", alias="MODEL_NAME")
    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")
    embed_model: str = Field(default="text-embedding-3-small", alias="EMBED_MODEL")

    # Data & index
    data_dir: str = "data/sample_docs"
    index_path: str = "index/faiss_index"
    chunk_size: int = 500
    chunk_overlap: int = 100
    k: int = 4

    class Config:
        env_file = ".env"

settings = Settings()
