
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

    # Connect to Milvus
connections.connect(
    alias="default",
    uri="https://in03-453b560d7b750a5.serverless.gcp-us-west1.cloud.zilliz.com",  # From cloud dashboard
    token="b6aecc2af232aa1c87f9a4b23482186cab8dd4dc4e41c328d3394ba37805d24d34f1da47278554eb38a98675912fd228d5d219b8"                                      # From API keys section
    )

    # Define schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=1024)  # Add text field
]

schema = CollectionSchema(fields, description="Chatbot Knowledge Base")

    # Create Collection
collection = Collection("chatbot_knowledge", schema)
collection.load()


