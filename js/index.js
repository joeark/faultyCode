import React, { useState } from 'react'

export default function Home() {
  const [counter, setCounter] = useState(0); 
  const handleClick = () => {
    setCounter(counter + 1);
    console.log("Counter:", counter + 1);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Counter App</h1>
      <p>Counter: {counter}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
}