import React, { useState } from 'react';
import useAPI from '../../hooks/useAPI';
import './DeckEditor.css';

function DeckEditor() {
  const [deckName, setDeckName] = useState('');
  const [deckDescription, setDeckDescription] = useState('');
  const [triggerAPI, setTriggerAPI] = useState(false);
  const createDeckURL = "http://127.0.0.1:8000/v1/deck/create";
  

  const { data, loading, error } = useAPI({
    method: 'POST',
    url: createDeckURL,
    body: { name: deckName, description: deckDescription},
  }, triggerAPI);
  
  console.log(data, loading, error, triggerAPI);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Trigger the API call
    setTriggerAPI(true);
    // If the API call is successful, reset the triggerAPI state
    if (data.message) {
      setTriggerAPI(false);
      setDeckName('');
      setDeckDescription('');
    }
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