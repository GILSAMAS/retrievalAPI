import React from 'react';
import Home from './Components/Pages/Home/Home.jsx';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Anki-like Application</h1>
            </header>
            <Home />
        </div>
    );
}

export default App;

// function App() {
//     const url = 'http://127.0.0.1:8000/v1/deck/list';

//     const {data, error, loading} = useAPI({
//         method:'GET', 
//         url: url, 
//     });

//     return (
//         <>
//         <h1>Decks</h1>
        // {loading && <p>Loading...</p>}
        // {error && <p>Error: {error.message}</p>}
//         {data && (
//             <ul>
//             {data.map(deck => (
//                 <li key={deck.id}>{deck.name}</li>
//             ))}
//             </ul>
//         )}
        
//         </>
//     );
// }

// export default App;