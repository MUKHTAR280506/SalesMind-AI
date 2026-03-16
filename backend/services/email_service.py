import smtplib
from email.mime.text import MIMEText

def send_invoice(order):

    
    message = f"""
Invoice

Product : {order.product_name}
Amount : ₹{order.price}

Payment ID : {order.payment_id}
Order ID : {order.order_id}

Thank you for your purchase.
"""
    
    msg = MIMEText(message)
    msg["Subject"]= "Your Invoice"
    msg["From"]= "your mail id "
    msg["To"]= order.email
   
    
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("your mail id ",'your app code')
    
    server.sendmail(
        "your mail id ",
        order.email,
        msg.as_string()
    )
    
    server.quit()

  
