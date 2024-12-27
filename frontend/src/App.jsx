import './App.css';
import Navbar from './Components/Pages/Navbar/Navbar';
import Footer from './Components/Pages/Footer/Footer';
import Sidebar from './Components/Pages/Sidebar/Sidebar';

function App({ children }) {

    return (
      <>
        <Navbar />
        <div className='app-content'>
          <Sidebar />
          {children}
        </div>
        <Footer />
      </>
    )
  }

export default App;
