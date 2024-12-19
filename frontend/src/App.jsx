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
      {/* <Card front="What's Data Science" back="Is the field of technology that allows you to get value from data" /> */}
    </>
  );
}

export default App;
