import { useState } from "react";
import ChatWindow from "./components/ChatWindow";
import Sidebar from "./components/Sidebar";
import "./App.css";

function App() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleNewMessage = async (message) => {
    setLoading(true);

    const res = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    setHistory(data.history);
    setLoading(false);
  };

  const clearHistory = async () => {
    await fetch("http://localhost:5000/clear", { method: "POST" });
    setHistory([]);
  };

  return (
    <div className="app">
      <div className="header">
        <h2>Mistral ChatBot</h2>
        <button onClick={clearHistory}>Clear History</button>
      </div>
      <div className="main">
        <Sidebar history={history} />
        <ChatWindow
          history={history}
          onSendMessage={handleNewMessage}
          loading={loading}
        />
      </div>
    </div>
  );
}

export default App;
