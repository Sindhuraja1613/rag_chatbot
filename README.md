# PDF Chatbot with Groq & FAISS
This project implements a basic Retrieval-Augmented Generation (RAG) pipeline that allows users to upload a PDF document and ask questions based on its contents.
## 🔥 Features
- **Document Processing🗂️**
  - PDF text extraction with metadata preservation
  - Intelligent chunking with configurable sizes
  - Sentence Transformer embeddings (all-MiniLM-L6-v2)
- **AI Capabilities🤖**
  - Groq-powered Llama3-70B responses
  - FAISS vector similarity search
  - Conversational memory
- **User Experience🕵️**
  - Streamlit web interface
  - Chat history preservation
  - Document source citations
## 📊Core Technologies

 | **Components** | **Tool/Library** |
|----------|----------|
| LLM      | Groq API with LLaMA 3   |
| Embeddings |Sentence Transformers (all-MiniLM-L6-v2)
|Vector Store | FAISS
|Framework| Langchain
|UI| Streamlit
## ⚡ configuration
The server can be configured through various settings in - [] -
 - GROQ_API_KEY
 - GROQ_MODEL
 - EMBEDDING_MODEL

## 🛠️ Project Structure
```sh
rag_chatbot/
├── app.py                 # Main application
├── modules/
│   ├── embeddings.py      # Custom embedding wrapper
│   ├── chains.py
│   ├── vector_store.py    # FAISS operations
│   └── document_processing.py
├── config/
    └── settings.py        # All configurations
```
## 📚Documentation
**How It Works🔧**
**Upload PDF Documents:**
1.Users upload PDF files via Streamlit's file uploader
2.Files are temporarily saved to ```pdfs```/ directory
**Tech Used:**
```PyPDFDirectoryLoader``` from LangChain
Streamlit's ```st.file_uploader()```

**System Processes and Chunks Text:**
1.PDFs are split into pages → paragraphs → semantic chunks
2.Configurable chunk size (default: 700 characters)
3.Preserves metadata (page numbers, source file)
**Tech Used:**
```RecursiveCharacterTextSplitter``` from LangChain

**Generates Vector Embeddings:**
1.Each text chunk is converted to a 768-dimension vector
2.Uses sentence-transformers'```all-MiniLM-L6-v2``` model
Ex:"Hello world" → ```[0.24, -0.35, ..., 0.72]```
**Tech Used:**
SentenceTransformer embeddings

**Stores in FAISS Index:**
1.Vectors are stored in optimized FAISS index
2.Metadata (original text + source info) saved separately

**Queries Answered via Groq LLM:**
1.User question → vector embedding
2.FAISS finds most relevant document chunks
3.Groq's Llama3 generates answer using retrieved context
 **Tech Used:**
Groq's ultra-fast inference API
LangChain's retrieval chain

**🎯Customization Options**
Change chunk size in settings.py :
```sh
CHUNK_SIZE = 700  # Characters per chunk(As per required)
```
Switch LLM model settings.py :
```sh
GROQ_MODEL = "llama3-8b-8192"  # Alternative model
```
**🤖 Example Queries**
"Summarize the key points of this document"
"What does section 3.2 say about compliance?"
"List all mentioned technologies"

# 📥Setup Instructions
## 1. Prerequisites

```sh 
Python 3.9+
Check your version:
python --version
Groq API Key (Free)
→  Get it https://console.groq.com/keys)here
```
## 2. Clone & Configure
A. Clone Repository
```
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot
```
B. Create Virtual Environment
Windows:
```
python -m venv venv
.\venv\Scripts\activate
```
Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```
C. Install Dependencies
```
pip install -r requirements.txt
```
D. Configure Environment
```
Create .env file:
echo "GROQ_API_KEY=your_api_key_here" > .env
```
Optional: Customize settings in .env:
```
.env
FAISS_INDEX_PATH=data/custom_index.index
CHUNK_SIZE=500  # Smaller chunks for precision
```
## 3. Run the Application
A. Start the Chatbot
```
streamlit run app.py
```
→ Opens at http://localhost:8501
```
```
B. First-Time Setup
```
1.Upload a PDF via sidebar
2.Click "Process PDF"
(Wait for "PDF processed" confirmation)
3.Start chatting!
```
##  📈Usage Workflow
**Access UI:**  Open http://localhost:8501
**Upload PDF:** Via sidebar uploader
**Process File:** Click "Process PDF" button
**Ask Questions:** Type in chat input

## 🧪Sample Use Cases
**Legal Document Analysis**
- Quick contract reviews
- Clause searching

**Academic Research**
- Paper summarization
- Cross-reference checking

**Enterprise Knowledge Base**
- Internal manual Q&A
- Onboarding helper
## ⚙️Troubleshooting

| Issue | Solution |
| ------ | ------ |
|GROQ_API_KEY missing|	Verify .env file exists
|FAISS not saving|	Check data/ directory permissions
|PDF processing fails|	Ensure file is not password-protected
|High RAM usage|	Reduce CHUNK_SIZE in settings.py
## 💡Coming Soon
- Multi-PDF support
- Hybrid search (keyword + vector)
- AWS S3 integration for cloud storage
## 🌟 Acknowledgments
For this Open-Source Project
*This project was made possible thanks to:*
- LangChain for the RAG framework
- Groq for their lightning-fast LLM inference
- The FAISS team at Meta for vector search
- Sentence-Transformers for embedding models

## 📄 License
🔓 Open Source under [MIT License](LICENSE)
## Author
Sindhu Raja
Email : sindhu.raja@bonbloc.com

