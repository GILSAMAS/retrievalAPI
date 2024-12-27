import React from 'react';
import './Sidebar.css';

function Sidebar({ selectedOption, setSelectedOption }) {
  return (
    <div className="sidebar">
      <h2>Options</h2>
      <ul>
        <li onClick={() => setSelectedOption('Decks')} className={selectedOption === 'Decks' ? 'active' : ''}>Decks</li>
        <li onClick={() => setSelectedOption('Stats')} className={selectedOption === 'Stats' ? 'active' : ''}>Stats</li>
      </ul>
    </div>
  );
}

export default Sidebar;