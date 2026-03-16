from sqlalchemy import Column, Text, Integer , String , DateTime ,Boolean
import datetime

from app.database import Base

class Product (Base):
    __tablename__ = "products"

    id = Column(Integer , primary_key=True)
    name = Column(String)
    price = Column(Integer)
    use_case = Column(String)
    category = Column(String)
    image = Column(String)


class Chat_history(Base):

    __tablename__ = "chat_history"

    
    id = Column(Integer, primary_key= True)
    session_id = Column(String)
    user_message = Column(String)
    bot_response = Column(String)
    created_at = Column(DateTime, default = lambda: datetime.datetime.now(datetime.timezone.utc))    

 
class Leads(Base):
   __tablename__ = "leads"

   id = Column(Integer, primary_key=True)
   name = Column(String)
   email = Column(String)
   product_name = Column(String)
   created_at = Column(DateTime, default = lambda: datetime.datetime.now(datetime.timezone.utc))



class Followup(Base):

    __tablename__ = "followups"

    id = Column(Integer , primary_key=True)
    email = Column(String)
    product_name = Column(String)
    message = Column(Text)  

class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    price = Column(String)
    email = Column(String)
    order_id = Column(String, default=None)
    payment_id = Column(String, default = None)
    payment_status = Column(Boolean , default = False) 
    invoice_sent = Column(Boolean, default= False)    