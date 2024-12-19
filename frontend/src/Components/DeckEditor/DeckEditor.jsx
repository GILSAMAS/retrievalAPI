import React, { useState } from 'react';
import './DeckEditor.css';

function DeckEditor({ onAddDeck }) {
  const [deckName, setDeckName] = useState('');
  const [deckDescription, setDeckDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onAddDeck({ name: deckName, description: deckDescription });
    setDeckName('');
    setDeckDescription('');
  };

  return (
    <form className="deck-editor" onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="deckName">Deck Name</label>
        <input
          type="text"
          id="deckName"
          value={deckName}
          onChange={(e) => setDeckName(e.target.value)}
          placeholder="Enter deck name"
        />
      </div>
      <div className="form-group">
        <label htmlFor="deckDescription">Deck Description</label>
        <textarea
          id="deckDescription"
          value={deckDescription}
          onChange={(e) => setDeckDescription(e.target.value)}
          placeholder="Enter deck description"
        />
      </div>
      <button type="submit">Create Deck</button>
    </form>
  );
}

export default DeckEditor;