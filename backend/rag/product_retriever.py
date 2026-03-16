from services.vector_service import search_products
from app.database import SessionLocal
from app.models import Product

def retrieve_products(query):
     
     ids = search_products(query)
     db = SessionLocal()

     products = db.query(Product).filter(Product.id.in_(ids)).all()

     result = []

     for p in products:
          result.append({
               "name": p.name,
               "price": f"₹{p.price:,}",
               "image": p.image
          })
     return result