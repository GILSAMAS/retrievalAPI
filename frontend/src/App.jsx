import './App.css';

function App({ children }) {

    return (
      <>
        <p>Navbar</p>
        {children}
        <p>Footer</p>
      </>
    )
  }

export default App;
