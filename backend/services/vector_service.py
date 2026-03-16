from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient("localhost", port=6333)

model = SentenceTransformer("all-MiniLM-L6-v2")

COLLECTION_NAME = "products"

def create_embedding(text):
    
    vector = model.encode(text)

    return vector

def search_products(query):

    query_vector = create_embedding(query)

    results = client.query_points(
               collection_name = COLLECTION_NAME,
               query = query_vector,
               limit =3
    )

    ids = [r.payload["product_id"] for r in results.points]

    return ids