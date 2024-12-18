import React, { useState } from 'react';
import './Card.css';

function Card({ front, back }) {
  const [isFlipped, setIsFlipped] = useState(false);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  return (
    <div className="card" onClick={handleFlip}>
      {isFlipped ? <div className="back">{back}</div> : <div className="front">{front}</div>}
    </div>
  );
}

export default Card;