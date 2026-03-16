from app.database import SessionLocal
from app.models import Leads

def save_lead(name, email, product):

    db = SessionLocal()

    lead = Leads(
        name= name,
        email= email,
        product_name= product
    )

    db.add(lead)
    db.commit()
    db.close()
    