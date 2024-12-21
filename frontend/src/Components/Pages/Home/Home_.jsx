import React, { useState } from 'react';
import useAPI from '../../../hooks/useAPI';
import './Home.css';

function Home() {
  const [selectedOption, setSelectedOption] = useState('Decks');
  const [selectedDeck, setSelectedDeck] = useState(null);
  const { data: decks, loading: decksLoading, error: decksError } = useAPI(
    {url:'http://127.0.0.1:8000/v1/deck/list',
     method: 'GET'});
  const { data: cards, loading: cardsLoading, error: cardsError } = useAPI({
    method: 'GET',
    url: selectedDeck ? `http://127.0.0.1:8000/v1/card/get_deck_cards/${selectedDeck.id}` : null
  }
  );

  const handleDeckClick = (deck) => {
    setSelectedDeck(deck);
  };

  const renderDecks = () => (
    <div>
      <h2>Available Decks</h2>
      <div className="deck-list">
        {decks && decks.map((deck) => (
          <div key={deck.id} className="deck-card" onClick={() => handleDeckClick(deck)}>
            <h3>{deck.name}</h3>
            <p>{deck.description}</p>
          </div>
        ))}
      </div>
      {selectedDeck && (
        <div className="card-list">
          <h3>Cards in "{selectedDeck.name}"</h3>
          {cardsLoading ? (
            <p>Loading cards...</p>
          ) : cardsError ? (
            <p>Error: {cardsError.message}</p>
          ) : cards && cards.length > 0 ? (
            cards.map((card) => (
              <div key={card.id} className="card">
                <div className="card-front" dangerouslySetInnerHTML={{ __html: card.front }}></div>
                {/* <div className="card-back" dangerouslySetInnerHTML={{ __html: card.back }}></div> */}
              </div>
            ))
          ) : (
            <p>No cards available in this deck.</p>
          )}
        </div>
      )}
    </div>
  );

  const renderStats = () => (
    <div>
      <h2>Stats</h2>
      {/* Add your stats components or content here */}
      <p>Stats content goes here.</p>
    </div>
  );

  if (decksLoading) return <p>Loading...</p>;
  if (decksError) return <p>Error: {decksError.message}</p>;

  return (
    <div className="home">
      <div className="options">
        <button
          className={selectedOption === 'Decks' ? 'active' : ''}
          onClick={() => { setSelectedOption('Decks'); setSelectedDeck(null); }}
        >
          Decks
        </button>
        <button
          className={selectedOption === 'Stats' ? 'active' : ''}
          onClick={() => setSelectedOption('Stats')}
        >
          Stats
        </button>
      </div>
      <div className="content">
        {selectedOption === 'Decks' && renderDecks()}
        {selectedOption === 'Stats' && renderStats()}
      </div>
    </div>
  );
}

export default Home;