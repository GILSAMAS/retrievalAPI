import React from 'react';
import './CardList.css';

function CardList({ cards, selectedDeck }) {
  return (
    <div className="cards-section">
      <h4>Cards in {selectedDeck.name}</h4>
      <ul>
        {cards.map(card => (
          <li key={card.id}>
            <div className="card-front">{card.front}</div>
            <div className="card-back">{card.back}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CardList;