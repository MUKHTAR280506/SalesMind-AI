import React, { useState } from "react";
import "./Chatbot.css";



function Chatbot() {

  const sessionId = "session_" + Math.random();
  const [messages, setMessages] = useState([
    { text: "Hi 👋 Welcome to TechNova Electronics! Ask me about our products.", sender: "bot" }
  ]);
  const [input, setInput] = useState("");

 const handleSend = async () => {
  if (!input.trim()) return;

  const userMessage = { text: input, sender: "user" };
  setMessages(prev => [...prev, userMessage]);

  try {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: input  , session_id: sessionId})
    });

    const data = await response.json();

    setTimeout(() => {
      setMessages(prev => [
        ...prev,
        { text: data.reply, sender: "bot" },
        ...(data.products.length > 0
          ? [{ products: data.products, sender: "bot", type: "products" }]
          : [])
      ]);
    }, 500);

     setInput("");

  } catch (error) {
    console.error(error);
  }

 
};

  return (
    <div className="app">
    <div className="chat-container">
      <div className="chat-header">TechNova Sales Assistant</div>

      <div className="chat-body">
        {messages.map((msg, index) => (
          <div key={index}>
            {msg.type === "products" ? (
              <div className="product-card-container">
                {msg.products.map((product, i) => (
                  <div key={i} className="product-card">
                    <img src={product.image} alt={product.name} />
                    <h4>{product.name}</h4>
                    <p>{product.price}</p>
                    <button>Buy Now</button>
                  </div>
                ))}
              </div>
            ) : (
              <div className={`message ${msg.sender}`}>
                {msg.text}
              </div>
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
          onKeyPress={(e) => e.key === "Enter" && handleSend()}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
    </div>
  );
}

export default Chatbot;