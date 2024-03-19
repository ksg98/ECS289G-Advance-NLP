// src/ChatBox.js
import React, { useState } from 'react';
import axios from 'axios';

const ChatBox = () => {
  const [message, setMessage] = useState('');
  const [conversation, setConversation] = useState([]);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!message.trim()) return;

    // Display user message immediately
    const newConversation = [...conversation, { sender: 'user', text: message }];
    setConversation(newConversation);

    try {
      const response = await axios.post('http://127.0.0.1:5000/chat', { prompt: message });
      // Access the first element of the array and then split the generated_text
      const systemMessage = response.data[0].generated_text.split('\n').slice(1).join('\n').trim();
      // Append response to conversation
      setConversation(conversation => [...conversation, { sender: 'system', text: systemMessage }]);
    } catch (error) {
      console.error('Error sending message:', error);
      setConversation(conversation => [...conversation, { sender: 'system', text: 'Error: Jailbreak prompt detected or server error.' }]);
    }

    setMessage(''); // Clear input field
};


  return (
    <div className="p-4">
      <div className="messages">
        {conversation.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={sendMessage} className="chat-form">
        <input
          type="text"
          className="input"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message here..."
        />
        <button type="submit" className="send-button">Send</button>
      </form>
    </div>
  );
};

export default ChatBox;
