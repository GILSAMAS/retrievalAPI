import React, { useContext } from 'react';
import { AppContext } from '../../../AppContextProvider.jsx';
import './Dashboard.css';

function Dashboard() {
  const { selectedOption, selectedDeck } = useContext(AppContext);

  console.log('Selected Deck:', selectedDeck);

  // Artificial data for cards
  const cards = [
    { id: 1, front: 'Card 1 Front', back: 'Card 1 Back' },
    { id: 2, front: 'Card 2 Front', back: 'Card 2 Back' },
    { id: 3, front: 'Card 3 Front', back: 'Card 3 Back' },
  ];

  return (
    <div className="dashboard">
      <div className="dashboard-content">
        {selectedDeck ? (
          <>
            <div className="top-section">
              <div className="main-content">
                <div className="deck-details">
                  <div className="deck-metadata">
                    <div className="deck-info">
                      <h2>{selectedDeck.name}</h2>
                      <p>{selectedDeck.description}</p>
                      <p>Tags: {selectedDeck.tags.join(', ')}</p>
                      <p>Created on: {selectedDeck.creationDate}</p>
                      <p>Last updated: {selectedDeck.lastUpdated}</p>
                    </div>
                    <div className="deck-actions">
                      <button>Rename</button>
                      <button>Study Now</button>
                      <button>Add New Card</button>
                      <button>Delete</button>
                    </div>
                  </div>
                </div>
              </div>
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
            </div>
            <div className="bottom-section">
              <h3>Score Over Time</h3>
              <div className="chart-placeholder">[Chart]</div>
            </div>
          </>
        ) : (
          <div className="default-content">
            <div className="search-bar">
              <input type="text" placeholder="Search..." />
            </div>
            <div className="content">
              {selectedOption === 'Decks' && <p>Decks content goes here.</p>}
              {selectedOption === 'Stats' && <p>Stats content goes here.</p>}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;