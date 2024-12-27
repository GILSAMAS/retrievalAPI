import React, { useContext } from 'react';
import { AppContext } from '../../../AppContextProvider.jsx';
import DeckMetadata from './DeckMetadata/DeckMetadata';
import CardList from './CardList/CardList';
import DeckPerformance from './DeckPerformance/DeckPerformance';
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
                <DeckMetadata selectedDeck={selectedDeck} />
              </div>
              <CardList cards={cards} selectedDeck={selectedDeck} />
            </div>
            <DeckPerformance />
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