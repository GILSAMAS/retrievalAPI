import React, { useState } from 'react';
// import CardEditor from './Components/CardEditor/CardEditor.jsx';
import DeckEditor from './Components/DeckEditor/DeckEditor.jsx';
import './App.css';

function App() {
  const [decks, setDecks] = useState([]);

  const handleAddDeck = (deckName) => {
    setDecks([...decks, { name: deckName, cards: [] }]);
    console.log('Decks:', decks);
  };

  return (
    <>
      <DeckEditor onAddDeck={handleAddDeck} />
    </>
  );
}

export default App;