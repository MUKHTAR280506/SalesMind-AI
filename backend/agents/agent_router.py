
def route_agent(query):

    q = query.lower()

    if "discount" in q:

        return "discount"
    
    if "buy" in q:

        return "checkout"
    
    if "invoice" in q:

        return "invoice"
    
    return "recommend"

