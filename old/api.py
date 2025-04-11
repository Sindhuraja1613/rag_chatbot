from fastapi import FastAPI, Query
from pymilvus import connections, Collection
from sentence_transformers import SentenceTransformer
import os
import uvicorn


app = FastAPI()

# Initialize models and connections
embedder = SentenceTransformer('all-MiniLM-L6-v2')  # Embedding model
connections.connect(alias="default",
uri="https://in03-453b560d7b750a5.serverless.gcp-us-west1.cloud.zilliz.com",  # From cloud dashboard
token="b6aecc2af232aa1c87f9a4b23482186cab8dd4dc4e41c328d3394ba37805d24d34f1da47278554eb38a98675912fd228d5d219b8"                                      # From API keys section
)  # Milvus connection
collection = Collection("chatbot_knowledge")     # Your Milvus collection

def retrieve_documents(query: str, top_k: int = 3):
    """Retrieve relevant documents from Milvus"""
    # Generate embedding
    query_embedding = embedder.encode([query])[0].tolist()
    
    # Search Milvus
    results = collection.search(
        data=[query_embedding],
        anns_field="embedding",  # Your vector field name
        param={"metric_type": "L2", "params": {"nprobe": 10}},
        limit=top_k,
        output_fields=["text"]   # Your text field name
    )
    
    return [hit.entity.get("text") for hit in results[0]]

@app.get("/chat")
async def chat(user_input: str = Query(...)):
    try:
        # Step 1: Retrieve relevant documents
        docs = retrieve_documents(user_input)
        
        # Step 2: Format context for LLM
        context = " ".join([f"- {doc}" for doc in docs])
        
        # Step 3: Generate response (replace with your LLM call)
        response = f"Context:{context} Question: {user_input} (Implement LLM call here)"
        
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
    
if __name__ == "__main__":
 uvicorn.run(app, host="0.0.0.0", port=8000)