import React, { useState } from 'react';
import Sidebar from '../Sidebar/Sidebar';
import './Dashboard.css';

function Dashboard() {
  const [selectedOption, setSelectedOption] = useState('Decks');

  return (
    <div className="dashboard">
      <Sidebar selectedOption={selectedOption} setSelectedOption={setSelectedOption} />
      <div className="main-content">
        <div className="search-bar">
          <input type="text" placeholder="Search..." />
        </div>
        <div className="content">
          {selectedOption === 'Decks' && <p>Decks content goes here.</p>}
          {selectedOption === 'Stats' && <p>Stats content goes here.</p>}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;