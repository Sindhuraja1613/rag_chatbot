from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings
from config.settings import settings


class CustomEmbeddings(Embeddings):
    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)
    
    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()
    
    def embed_query(self, text):
        return self.model.encode(text).tolist()