from app.database import SessionLocal
from app.models import Followup

def create_followup(email, product):

    db = SessionLocal()

    message = f"We noticed you were interested in {product} Limited discount available"

    f = Followup(
        email = email,
        product_name = product,
        message = message
    )

    db.add(f)
    db.commit()
    db.close()