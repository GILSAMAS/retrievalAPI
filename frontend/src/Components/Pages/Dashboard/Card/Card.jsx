import React from 'react';
import './Card.css';

function Card({ card }) {
  return (
    <div className="card">
      <div className="card-front">{card.front}</div>
      <div className="card-actions">
        <button>Update</button>
        <button>Delete</button>
      </div>
    </div>
  );
}

export default Card;