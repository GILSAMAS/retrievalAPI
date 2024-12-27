import React from 'react';
import Card from '../Card/Card';
import './CardList.css';

function CardList({ cards, selectedDeck }) {
  return (
    <div className="cards-section">
      <h4>Cards in {selectedDeck.name}</h4>
      <ul>
        {cards.map(card => (
          <li key={card.id}>
            <Card card={card} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CardList;