from app.database import engine
from app.models import Base
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    name: str | None = None
    price: str | None = None
    email: str | None = None
    session_id: str

class LeadRequest(BaseModel):
    name: str
    email: str
    product: str

class OrderRequest(BaseModel):
    product_name: str
    price: str
    email: str    

def init_db():

   Base.metadata.create_all(bind=engine)
