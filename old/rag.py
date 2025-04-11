from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_documents(query):
    query_embedding = embed_model.encode([query]).tolist()
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    
    results = collection.search(query_embedding, "embedding", search_params, limit=3, output_fields=["id"])
    
    docs = [result.entity for result in results[0]]
    return docs
