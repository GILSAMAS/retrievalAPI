import {BrowserRouter, Navigate, Route, Routes} from 'react-router-dom';
import Login from './Components/Pages/Login/Login';
import Home from './Components/Pages/Home/Home__.jsx';
import Dashboard from './Components/Pages/Dashboard/Dashboard.jsx';
function AppRouter() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/"  element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/dashboard" element={<Dashboard />} />
            </Routes>
        </BrowserRouter>
    );
}

export default AppRouter;