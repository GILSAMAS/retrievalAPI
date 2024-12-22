import React, { useState } from 'react';
import useAPI from '../../../hooks/useAPI';
import DeckEditor from '../../DeckEditor/DeckEditor';
import CardEditor from '../../CardEditor/CardEditor';
import './Home.css';

function Home() {
  const [selectedOption, setSelectedOption] = useState('Decks');
  const [selectedDeck, setSelectedDeck] = useState(null);
  const [showCardEditor, setShowCardEditor] = useState(false);

  const { data: decks, loading: decksLoading, error: decksError } = useAPI({
    url: 'http://127.0.0.1:8000/v1/deck/list',
    method: 'GET'
  });

  const { data: cards, loading: cardsLoading, error: cardsError } = useAPI({
    method: 'GET',
    url: selectedDeck ? `http://127.0.0.1:8000/v1/card/get_deck_cards/${selectedDeck.id}` : null
  });

  const handleDeckClick = (deck) => {
    setSelectedDeck(deck);
    setShowCardEditor(false);
  };

  const handleAddCard = (card) => {
    // Add the new card to the selected deck's cards
    setSelectedDeck((prevDeck) => ({
      ...prevDeck,
      cards: [...prevDeck.cards, card]
    }));
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
          <button onClick={() => setShowCardEditor(true)}>Create Card</button>
          {showCardEditor && <CardEditor onAddCard={handleAddCard} />}
          {cardsLoading ? (
            <p>Loading cards...</p>
          ) : cardsError ? (
            <p>Error: {cardsError.message}</p>
          ) : cards && cards.length > 0 ? (
            cards.map((card) => (
              <div key={card.id} className="card">
                <div className="card-front" dangerouslySetInnerHTML={{ __html: card.front }}></div>
                <div className="card-back" dangerouslySetInnerHTML={{ __html: card.back }}></div>
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


  const renderCreateDeck = () => (
    <div>
      <h2>Create Deck</h2>
      <DeckEditor/>
    </div>
  );

  if (decksLoading) return <p>Loading...</p>;
  if (decksError) return <p>Error: {decksError.message}</p>;

  return (
    <div className="home">
      <div className="options">
        <button
          className={selectedOption === 'Decks' ? 'active' : ''}
          onClick={() => { setSelectedOption('Decks'); setSelectedDeck(null); setShowCardEditor(false); }}
        >
          Decks
        </button>
        <button
          className={selectedOption === 'Create Deck' ? 'active' : ''}
          onClick={() => { setSelectedOption('Create Deck'); setSelectedDeck(null); setShowCardEditor(false); }}
        >
          Create Deck
        </button>
        <button
          className={selectedOption === 'Stats' ? 'active' : ''}
          onClick={() => { setSelectedOption('Stats'); setSelectedDeck(null); setShowCardEditor(false); }}
        >
          Stats
        </button>
      </div>
      <div className="content">
        {selectedOption === 'Decks' && renderDecks()}
        {selectedOption === 'Create Deck' && renderCreateDeck()}
        {selectedOption === 'Stats' && renderStats()}
      </div>
    </div>
  );
}

export default Home;