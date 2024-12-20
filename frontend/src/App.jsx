import React from 'react';
import useFetch from './hooks/useFetch';
import './App.css';

function App() {
    const url = 'http://127.0.0.1:8000/v1/deck/list';
    const { data: decks, loading, error } = useFetch(url);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}</p>;

    return (
        <>
        <h1>Decks</h1>
        {decks && decks.map((deck, index) => (
            <div key={index}>
            <h2>{deck.name}</h2>
            <p>{deck.description}</p>
            </div>
        ))}
        </>
    );
}

export default App;