import streamlit as st
import os
from langchain_groq import ChatGroq
from modules.vector_store import VectorStore
from modules.document_processing import load_and_split_pdfs
from modules.chains import get_qa_chain
from config.settings import settings

# Initialize components
def initialize():
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = VectorStore()
    if "llm" not in st.session_state:
        st.session_state.llm = ChatGroq(
            model=settings.GROQ_MODEL,
            temperature=0.3,
            api_key=settings.GROQ_API_KEY
        )
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

# File upload handler
def handle_file_upload(uploaded_file):
    if uploaded_file:
        pdf_dir = "pdfs"
        os.makedirs(pdf_dir, exist_ok=True)
        file_path = os.path.join(pdf_dir, uploaded_file.name)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        documents = load_and_split_pdfs(pdf_dir)
        
        st.session_state["last_uploaded_docs"] = documents  # <-- Store for summarization

        if st.session_state.vector_store.create_store(documents):
            st.success("PDF processed and ready for questions!")
        else:
            st.error("Failed to process PDF")


# Main UI
def main():
    st.title("📄 RAG CHATBOT")
    st.markdown("Upload a PDF and ask questions about its content")
    
    initialize()
    
    # Sidebar for uploads
    with st.sidebar:
        st.header("Upload PDF")
        uploaded_file = st.file_uploader(
            "Choose a PDF file", 
            type=["pdf"],
            accept_multiple_files=False
        )
        
        if uploaded_file and st.button("Process PDF"):
            with st.spinner("Processing PDF..."):
                handle_file_upload(uploaded_file)
        
    
    # Main chat interface
    user_question = st.chat_input("Ask a question about the PDF")
    
    if user_question:
        if not st.session_state.vector_store.vector_store:
            st.warning("Please upload and process a PDF first")
            return
        
        retriever = st.session_state.vector_store.get_retriever()
        qa_chain = get_qa_chain(st.session_state.llm)
        
        with st.spinner("Thinking..."):
            response = qa_chain.invoke({
                "input": user_question,
                "context": retriever.get_relevant_documents(user_question)
            })
        
        st.session_state.chat_history.append({
            "question": user_question,
            "answer": response
        })
        
        # Display chat history
        for chat in st.session_state.chat_history:
            with st.chat_message("user"):
                st.write(chat["question"])
            with st.chat_message("assistant"):
                st.write(chat["answer"])

if __name__ == "__main__":
    main()