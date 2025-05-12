import { useState } from "react";

function ChatWindow({ history, onSendMessage, loading }) {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    onSendMessage(input);
    setInput("");
  };

  return (
    <div className="chat-window">
      <div className="messages">
        {history.map((msg, i) => (
          <p key={i}>
            <strong>{msg.role}: </strong> {msg.content}
          </p>
        ))}
        {loading && (
          <p>
            <strong>assistant:</strong> <i>Loading..</i>
          </p>
        )}
      </div>
      <div className="input-chat">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your question..."
        />
        <div>
          <button onClick={handleSend}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default ChatWindow;
