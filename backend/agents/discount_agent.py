def calculate_discount (product):

    price = int(product.replace("₹","").replace(",",""))

    if price > 70000:
        return 10
    
    if price > 50000:
        return 7
    
    return 5
