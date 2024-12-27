import React from 'react';
import './Navbar.css';

function Navbar() {
  return (
    <div className="navbar">
      <div className="navbar-brand">
        ReviseAI
      </div>
      <div className="navbar-options">
        <a href="/">Home</a>
        <a href="/profile">Profile</a>
        <a href="/logout">Logout</a>
      </div>
    </div>
  );
}

export default Navbar;