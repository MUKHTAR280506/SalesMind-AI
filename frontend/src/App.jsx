import React from "react";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Chatbot from "./components/Chatbot";
import Analytics from "./components/Analytics";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Chatbot/>} />
        <Route path="/analytics" element= {<Analytics />} />
      </Routes>
    </Router>
  
  )
}

export default App;