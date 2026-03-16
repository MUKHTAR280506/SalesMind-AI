import React, { useState , useRef} from "react";
import "./Chatbot.css";

function Chatbot() {
 
const API_BASE = "  https://efda-2401-4900-1c3c-62c2-3ceb-a70e-fd79-5ebb.ngrok-free.app/api";     

const sessionIdRef = useRef("session_" + Math.random());

const [messages, setMessages] = useState([
{ text: "Hi 👋 Welcome to TechNova Electronics!", sender: "bot" }
]);

const [input, setInput] = useState("");

const [selectedProduct, setSelectedProduct] = useState(null);

const handleSend = async () => {

if (!input.trim()) return;

const userMessage = { text: input, sender: "user" };

setMessages(prev => [...prev, userMessage]);

const response = await fetch("  https://efda-2401-4900-1c3c-62c2-3ceb-a70e-fd79-5ebb.ngrok-free.app/api/chat", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({
message: input,
session_id: sessionIdRef.current
})
});

const data = await response.json();

setMessages(prev => [
...prev,
{ text: data.reply, sender: "bot" },
...(data.products.length > 0
? [{ products: data.products, sender: "bot", type: "products" }]
: [])
]);

setInput("");

};

const captureLead = async (product) => {

const name = prompt("Enter your name");

const email = prompt("Enter your email");

await fetch("  https://efda-2401-4900-1c3c-62c2-3ceb-a70e-fd79-5ebb.ngrok-free.app/api/lead", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({
name: name,
email: email,
product: product
})
});

alert("Thanks! Our sales team will contact you.");

};

// add buy button click logic


const createOrder = async (product) => {
  const email = prompt("Enter your Email id to recieve the invoice")
  const res = await fetch("https://efda-2401-4900-1c3c-62c2-3ceb-a70e-fd79-5ebb.ngrok-free.app/api/create-order", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      product_name: product.name,
      price: product.price,
      email: email,
      
    })
  });

  const data = await res.json();

  openRazorpay(data);
};

const openRazorpay = (order) => {

  const options = {
    key: order.key,
    amount: order.amount,
    currency: "INR",
    order_id: order.order_id,

    handler: async function (response) {

      const verify = await fetch("https://efda-2401-4900-1c3c-62c2-3ceb-a70e-fd79-5ebb.ngrok-free.app/api/verify-payment",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(response)
      });

      const data = await verify.json();

      
      setMessages(prev => [...prev, { text: data.reply, sender: "bot" }
                              ]);
      
    }
  };

  const rzp = new window.Razorpay(options);
  rzp.open();
};


return (
  <div className="app">

    <div className="chat-container">

      <div className="chat-header">AI Sales Assistant</div>

      <div className="chat-body">

        {messages.map((msg, index) => (

          <div key={index} className={`message ${msg.sender}`}>

            {msg.type === "products" ? (

              <div className="product-card-container">

                {msg.products.map((product, i) => (

                  <div key={i} className="product-card">

                    <img src={`${API_BASE}${product.image}`} alt={product.name} />

                    <h4>{product.name}</h4>

                    <p>{product.price}</p>

                    <button onClick={() => createOrder(product)}>
                      Buy Now
                    </button>

                  </div>

                ))}

              </div>

            ) : (

              <>
                <div>{msg.text}</div>

                {msg.payment_link && (
                  <a href={msg.payment_link} target="_blank" rel="noopener noreferrer">
                    <button className="pay-btn">Pay Now</button>
                  </a>
                )}
              </>

            )}

          </div>

        ))}

      </div>

      <div className="chat-footer">

        <input
          type="text"
          placeholder="Type your message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />

        <button onClick={handleSend}>Send</button>

      </div>

    </div>

  </div>
);
}
export default Chatbot;