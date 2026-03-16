





SalesMind AI – Intelligent Conversational Sales Assistant

SalesMind AI is a full-stack AI-powered sales chatbot that helps users discover products, get recommendations, and complete purchases through a conversational interface.The system combines Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), vector search, and real-time payments to create an intelligent shopping assistant. The chatbot can answer product questions, recommend items, capture leads, and process payments seamlessly.

-----Features

AI Conversational Sales Assistant

Natural language product search

AI-powered responses using locally hosted LLMs

Intelligent product recommendations

---------Retrieval Augmented Generation (RAG)

Product knowledge retrieved using vector search

Context-aware responses using Qdrant vector database

------- Product Discovery

AI understands customer intent

Shows product cards inside chat

Image, price, and buy button

--------Payment Integration

Integrated with Razorpay Checkout

Secure payment verification

Automatic invoice generation

--------Automated Order Processing

Payment confirmation

Order stored in PostgreSQL

Invoice sent to customer email

--------Context Memory

Session-based chat conversations

Context retained for product recommendations

---------Lead Capture

Customer name and email captured

Lead stored in database



System Architecture : --------


User (React Chat UI)
        │
        ▼
FastAPI Backend (API Layer)
        │
        ├── Ollama LLM (AI responses)
        │
        ├── Qdrant Vector DB (Product embeddings)
        │
        ├── PostgreSQL (Orders + Leads)
        │
        └── Razorpay API (Payments)

AI Stack : --------

The chatbot uses a modern AI architecture combining:

Large Language Model- phi3:mini (less data consumption , can be trained in GPU)

Ollama

Local LLM inference

Retrieval Augmented Generation

Qdrant Vector Database

Semantic product search

Embeddings

Product data embedded for vector search

Tech Stack : --------------

Backend -:

FastAPI

Python

SQLAlchemy

PostgreSQL

AI Stack

Ollama

RAG (Retrieval Augmented Generation)

Qdrant Vector Database


Frontend -:

React

Vite

CSS

Payments

Razorpay Checkout API

Infrastructure

Ngrok (for webhook testing)-- for real time experience

📂 Project Structure
SalesMind-AI
│
├── backend
│   
|   index_products.py
|   intent_model.pkl
|   train_intent_model.py
|   vectorizer.pkl
|   
+---agents
|   |   agent_router.py
|   |   discount_agent.py
|   |   sales_agent.py
|   |   
|           
+---app
|   |   database.py
|   |   main.py
|   |   models.py
|   |   schemas.py
|           
+---images
|       
|       
+---nlp
|   |   intent_classifier.py
|   |   spacy_extractor.py
|   |   
|           
+---rag
|   |   product_retriever.py
|   |   
|   
+---services
|   |   checkout_service.py
|   |   email_service.py
|   |   followup_service.py
|   |   lead_service.py
|   |   llm_service.py
|   |   memory_service.py
|   |   payment_service.py
|   |   product_service.py
|   |   vector_service.py
|   |   
        

│
├── frontend
│   ├── src
│   │   ├── Chatbot.jsx
│   │   ├── App.jsx
│   │   └── Chatbot.css
│
├── requirements.txt
└── README.md
|__ .env


⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/mukhtar280506/salesmind-ai.git
cd salesmind-ai

Backend Setup:
Create Virtual Environment
python -m venv venv

Activate environment

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Setup PostgreSQL

Create database

salesdb

Update connection string in:

database.py
Setup Qdrant

Run Qdrant locally

docker run -p 6333:6333 qdrant/qdrant
Setup Ollama

Install Ollama

https://ollama.com

Pull model

ollama pull phi3:mini

Start Ollama

ollama serve

Setup Razorpay

Create Razorpay account

https://razorpay.com

Add ID and API keys in .env

RAZORPAY_KEY_ID=your_key
RAZORPAY_SECRET=your_secret

Run Backend
cd backend
uvicorn app.main:app --reload

Server runs at

http://localhost:8000

Frontend Setup

Go to frontend folder

cd frontend

Install dependencies

npm install

Start React app

npm run dev

Frontend runs at

http://localhost:

to access the application from internet. USE ngrok. run ngrok command " ngrok http 5173" this will map your localhost to Internet and can be accessed from any where. 

modify vite.config.ts as 
"""
export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    allowedHosts: true,
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, "")
      }
    }
  }
})
"""

in react chatbot.jsx replace Internet URL/api (received from ngrok) with http://localhost:5173 

Payment Flow:-

User selects product in chatbot

React requests order creation

FastAPI creates Razorpay order

Razorpay Checkout popup opens

User completes payment

Backend verifies payment signature

Order updated in database

Invoice sent to user email


Security Features-----


Payment signature verification

Secure Razorpay order validation

Session-based conversation management



 Future Improvements-----

WhatsApp chatbot integration

Voice-based shopping assistant

AI sales analytics dashboard

Multi-language support

Personalized product recommendations

Admin dashboard for sales insights

👨‍💻 Author

Mukhtar Ahmad

AI Chatbot Developer 

LinkedIn
https://www.linkedin.com/in/mukhtar280506/

GitHub
https://github.com/MUKHTAR280506



