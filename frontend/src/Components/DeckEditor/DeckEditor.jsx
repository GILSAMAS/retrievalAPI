import React, { useState } from 'react';
import useAPI from '../../hooks/useAPI';
import './DeckEditor.css';

function DeckEditor() {
  const [deckName, setDeckName] = useState('');
  const [deckDescription, setDeckDescription] = useState('');
  const { data, loading, error, makeRequest } = useAPI();
  const createDeckURL = "http://127.0.0.1:8000/v1/deck/create";

  const handleSubmit = async (e) => {
    e.preventDefault();
    await makeRequest({
      method: 'POST',
      url: createDeckURL,
      body: { name: deckName, description: deckDescription },
    });

    // Reset the form only if the request was successful
    if (data && data.message) {
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
      <button type="submit" disabled={loading}>
        {loading ? 'Creating...' : 'Create Deck'}
      </button>
      {error && <p className="error">Error: {error.message}</p>}
      {data && data.message && <p className="success">{data.message}</p>}
    </form>
  );
}

export default DeckEditor;
