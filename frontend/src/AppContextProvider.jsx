import React, { createContext, useState } from 'react';

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [selectedOption, setSelectedOption] = useState('Decks');
  const [selectedDeck, setSelectedDeck] = useState(null);

  return (
    <AppContext.Provider value={{ selectedOption, setSelectedOption, selectedDeck, setSelectedDeck }}>
      {children}
    </AppContext.Provider>
  );
};