// import { useState } from 'react'
import React from 'react';
import Card from "./Components/Card/Card.jsx";
import CardEditor from "./Components/CardEditor/CardEditor.jsx";
import './App.css';

function App() {
  const onAddCard = ({front, back}) => {
    console.log('Front:', front);
    console.log('Back:', back);
  };
  return (
    <>
      <CardEditor onAddCard={onAddCard} />
    </>
  );
}

export default App;
