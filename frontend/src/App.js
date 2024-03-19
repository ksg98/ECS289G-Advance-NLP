// src/App.js
import React from 'react';
import './App.css';
import ChatBox from './ChatBox.js';

function App() {
  return (
    <div className="App">
      <div className="landing-page p-5 text-center">
        <h1 className="text-3xl font-bold mb-4">StopDAN: Enhancing LLM Security</h1>
        <p className="mb-6">
          Our project presents a groundbreaking framework aimed at bolstering the security measures
          of Large Language Models (LLMs) against sophisticated jailbreak attacks. By integrating
          advanced detection mechanisms with dynamic mitigation strategies, we propose a solution
          that is both scalable and adaptable to the evolving landscape of cyber threats targeting LLMs.
          Leveraging a meticulously compiled dataset, our approach is designed to enhance the resilience
          of LLMs across various implementations, ensuring their safe and ethical application in real-world scenarios.
        </p>
      </div>
      <ChatBox />
    </div>
  );
}

export default App;
