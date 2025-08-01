import React, { useState } from 'react';

function Generator() {
  const [prompt, setPrompt] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setResult(data.generated);
    } catch (error) {
      console.error('Error:', error);
      setResult('Error generating text');
    }
  };

  return (
    <div>
      <h2>Text Generator</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter a prompt"
        />
        <button type="submit">Generate</button>
      </form>
      {result && (
        <div>
          <h3>Generated Text:</h3>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
}

export default Generator;