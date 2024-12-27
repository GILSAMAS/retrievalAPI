import React, { useState, useContext } from 'react';
import { AppContext } from '../../../AppContextProvider.jsx';
import './Sidebar.css';

function Sidebar() {
  const { selectedOption, setSelectedOption, selectedDeck, setSelectedDeck } = useContext(AppContext);
  const [isAccordionOpen, setIsAccordionOpen] = useState(false);

  // Artificial data for decks
  const decks = [
    { id: 1, name: 'Deck 1', description: 'Description for Deck 1', tags: ['tag1', 'tag2'], creationDate: '2023-01-01', lastUpdated: '2023-01-10' },
    { id: 2, name: 'Deck 2', description: 'Description for Deck 2', tags: ['tag3'], creationDate: '2023-02-01', lastUpdated: '2023-02-10' },
    { id: 3, name: 'Deck 3', description: 'Description for Deck 3', tags: ['tag4', 'tag5'], creationDate: '2023-03-01', lastUpdated: '2023-03-10' },
  ];

  const handleAccordionToggle = () => {
    setIsAccordionOpen(!isAccordionOpen);
  };

  return (
    <div className="sidebar">
      <h2>Options</h2>
      <ul>
        <li onClick={() => { setSelectedOption('Decks'); handleAccordionToggle(); }} className={selectedOption === 'Decks' ? 'active' : ''}>
          Decks {isAccordionOpen ? '' : ''}
        </li>
        {isAccordionOpen && selectedOption === 'Decks' && (
          <ul className="accordion-content">
            {decks.map(deck => (
              <li key={deck.id} onClick={() => setSelectedDeck(deck)} className={selectedDeck && selectedDeck.id === deck.id ? 'active' : ''}>
                {deck.name}
              </li>
            ))}
          </ul>
        )}
        <li onClick={() => setSelectedOption('Stats')} className={selectedOption === 'Stats' ? 'active' : ''}>Stats</li>
      </ul>
    </div>
  );
}

export default Sidebar;