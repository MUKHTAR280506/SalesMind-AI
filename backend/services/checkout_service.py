import uuid

def generate_checkout(product , price):

    order_id = str(uuid.uuid4())

    checkout_link = f"http://localhost:8000/checkout/{order_id}"

    return checkout_link