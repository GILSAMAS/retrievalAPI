import React from 'react';
import './DeckMetadata.css';

function DeckMetadata({ selectedDeck }) {
  return (
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
  );
}

export default DeckMetadata;