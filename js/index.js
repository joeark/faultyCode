
import React from 'react'

export default function Home() {
  let counter = 0; 
  const handleClick = () => {
    counter += 1;
    console.log("Counter:", counter);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Counter App</h1>
      <p>Counter: {counter}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
}
