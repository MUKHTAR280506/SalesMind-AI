import React , {useState} from 'react';
import "./Chatbot.css"

const faqResponses = {
    "hello" : " Hi Welcome to TechNova Electronics ! How can I help you today",
    "laptop": "We have gaming, business, and budget laptops. What is your budget ?",
    "price of iphone": "The iPhone 15 starts at Rs 79000",
    "return policy" : "We offer a 7-day easy return policy",
    "contact": "You can contact us at support@technova.com"
};


function Chatbot() {
    const [messages, setMessages] = useState([
        {text: "Hi Welcome to Technova Electronics! Aske me about our Products.", sender: "bot"}
    ]);

    const [input, setInput]= useState("");

    const handleSend = () => {
        if(! input.trim()) return ;
        
        const userMessage = {text : input, sender: "user"}
        setMessages([...messages, userMessage]);
        
        const lowerInput =input.toLowerCase();

        let botReply = " Sorry , I did not understand that. Please ask about Products"

        for (let key in faqResponses) {
            if (lowerInput.includes(key)) {
                botReply = faqResponses[key];
                break;
            }
        }

        setTimeout (() => {
            setMessages(prev => [...prev , {text : botReply, sender: "bot"}]);
        }, 200);

        setInput("");
    };

    return (
       <div className="app"> 
        <div className="chat-container">
            <div className="chat-header" >TechNova Sales Chatbot</div>

            <div className='chat-body'>
              {messages.map ((msg, index)=>(
                <div key={index} className = {`message ${msg.sender}`}>
                    {msg.text}
                </div>    
              ))}
            </div>

            <div className ="chat-footer">
               <input 
               type="text"
               placeholder='Type your message'
               value={input}
               onChange={(e)=> setInput(e.target.value)}
               onKeyDown={(e)=>e.key ==="Enter" && handleSend()}
               />
               <button onClick={handleSend}>Send</button> 
            </div>

        </div>
      </div>  
    )
}

export default Chatbot;