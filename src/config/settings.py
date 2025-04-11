import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # FAISS Configuration
    FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "data/faiss_index.index")
    FAISS_METADATA_PATH = os.getenv("FAISS_METADATA_PATH", "data/faiss_metadata.pkl")
    EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION", "768"))
    
    # Groq Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Required
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")
    
    # Embedding Model
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    
    # Document Processing
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "5000"))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "2000"))

settings = Settings()