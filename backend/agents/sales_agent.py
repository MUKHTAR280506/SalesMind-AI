from services.product_service import get_products

def decide_action(query):

    query = query.lower()

    if "buy" in query :
        return "recommend"
    
    if "price" in query :
        return "recommend"
    
    if "contact" in query:
        return "lead"
    
    return "chat"