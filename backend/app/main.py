from fastapi import FastAPI , Request, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from .database import SessionLocal
from .schemas import ChatRequest, LeadRequest, init_db, OrderRequest
from nlp.intent_classifier import predict_intent
from nlp.spacy_extractor import extract_entities
from services.product_service import get_products
from fastapi.middleware.cors import CORSMiddleware
from rag.product_retriever import retrieve_products
from services.llm_service import generate_sales_response
from services.lead_service import save_lead
from agents.sales_agent import decide_action
from services.memory_service import save_chat , get_recent_context
from fastapi.staticfiles import StaticFiles
from services.followup_service import create_followup
from services.email_service import send_invoice
# from services.checkout_service import generate_checkout
from services.payment_service import generate_checkout
from agents.discount_agent import calculate_discount
from agents.agent_router import route_agent
from fastapi_utils.tasks import repeat_every
from .models import Leads, Orders
import requests
import os
import razorpay
from dotenv import load_dotenv

session_products = {}
app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")
load_dotenv()
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")

client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET)
)


@app.on_event("startup")
def on_startup():
    init_db()



    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    


# ----- Chat Endpoint -----
@app.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
   
   
   query= request.message.lower()
   agent = route_agent(query)
   session_id = request.session_id
   
   action = decide_action(query)

   if agent =="recommend":
       
    products = retrieve_products(query)
    print(products)
    session_products[session_id]=products
    reply = generate_sales_response(query, products)

    save_chat(session_id, query , reply)

    return {
       "reply": reply,
       "products": products
    }
  
  
   if agent == "discount":
       
       n=0
       
       products = session_products.get(session_id,[])
       print(products)
       for product in products:
            print(product)
            print(product['price'])
            discount = calculate_discount(product["price"])
            new_price = int(products[n]["price"].replace("₹","").replace(",","")) - int(products[n]["price"].replace("₹","").replace(",","")) *discount /100
            products[n]["price"]="₹"+str(new_price)
            n+=1

       n=0    

       

       return {
           "reply": f" Below are the discounted price for the following products.",
           "products" : products
       }
   
   
@app.post("/create-order")
def create_order(order: OrderRequest, db: Session = Depends(get_db)):

    order_data = client.order.create({
        "amount": 200 * 100,
        "currency": "INR",
        "payment_capture": 1
    })

    db_order = Orders(
        product_name=order.product_name,
        price=order.price,
        email=order.email,
        order_id=order_data["id"]
    )

    db.add(db_order)
    db.commit()

    return {
        "order_id": order_data["id"],
        "amount": order_data["amount"],
        "key": RAZORPAY_KEY_ID
    }


@app.post("/verify-payment")
def verify_payment(data: dict, db: Session = Depends(get_db)):

    params = {
        "razorpay_order_id": data["razorpay_order_id"],
        "razorpay_payment_id": data["razorpay_payment_id"],
        "razorpay_signature": data["razorpay_signature"]
    }

    client.utility.verify_payment_signature(params)

    order = db.query(Orders).filter(
        Orders.order_id == data["razorpay_order_id"]
    ).first()

    order.payment_status = True
    order.payment_id = data["razorpay_payment_id"]

    send_invoice(order)

    order.invoice_sent = True

    db.commit()

    return {"reply": f""" Payment successful.

           Payment ID: {params["razorpay_payment_id"]}
           Order ID: {params["razorpay_order_id"]}

           Invoice has been sent to {order.email}
           """
            }

# --------Leads endpoint -----------------
@app.post("/lead")
def lead(request: LeadRequest):

    save_lead(
        request.name,
        request.email,
        request.product
    )

    return {"message": "Lead captured"}

# ------- Analytics endpoint ----------

@app.get("/analytics")
def analytics():

    db = SessionLocal()

    total_chats = db.execute(
        text("SELECT COUNT(*) FROM chat_history")
    ).scalar()

    total_leads = db.execute(
        text("SELECT COUNT(*) FROM leads")
    ).scalar()

    top_products = db.execute(
        text("""
        SELECT product_name, COUNT(*) as count
        FROM leads
        GROUP BY product_name
        ORDER BY count DESC
        LIMIT 5
        """)
    ).fetchall()

    db.close()

    return {
        "total_chats": total_chats,
        "total_leads": total_leads,
        "top_products": [
            {"product": row[0], "count": row[1]}
            for row in top_products
        ]
    }

