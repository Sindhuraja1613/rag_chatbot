from langchain_community.vectorstores import FAISS
from modules.empeddings import CustomEmbeddings
import streamlit as st

class VectorStore:
    def __init__(self):
        self.embeddings = CustomEmbeddings()
        self.vector_store = None
    
    def create_store(self, documents):
        """Create FAISS vector store from documents"""
        if documents:
            self.vector_store = FAISS.from_documents(
                documents,
                self.embeddings
            )
            return True
        return False
    
    def get_retriever(self):
        """Get retriever for the vector store"""
        return self.vector_store.as_retriever() if self.vector_store else None