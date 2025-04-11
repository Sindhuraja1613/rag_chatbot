from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_and_split_pdfs(pdf_dir="pdfs"):
    """Load and split PDF documents"""
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
        return []
    
    loader = PyPDFDirectoryLoader(pdf_dir)
    docs = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=5000,
        chunk_overlap=2000
    )
    return splitter.split_documents(docs)