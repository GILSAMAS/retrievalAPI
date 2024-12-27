import './App.css';
import Navbar from './Components/Pages/Navbar/Navbar';
import Footer from './Components/Pages/Footer/Footer';

function App({ children }) {

    return (
      <>
        <Navbar />
        {children}
        <Footer />
      </>
    )
  }

export default App;
