from sqlalchemy.orm import Session
from app.models import Product

def get_products (db:Session, budget= None, use_case=None):

    query = db.query(Product)

    if budget:
        query = query.filter(Product.price <= budget)

    if use_case:
        query = query.filter(Product.use_case == use_case )

    return query.all()        