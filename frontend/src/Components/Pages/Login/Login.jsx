import "./Login.css";

function Login() {
    return (
        <div className="login">
            <h1>Login</h1>
            <form>
                <div className="form-group">
                    <label htmlFor="username">Email</label>
                    <input type="text" id="username" placeholder="Enter Email" className="input-field"/>
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input type="password" id="password" placeholder="Enter password" className="input-field"/>
                </div>
                <button type="submit" className="submit-button">Login</button>
            </form>
        </div>
    );
}

export default Login;