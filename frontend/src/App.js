import React, { useState } from 'react';
import LoginForm from './LoginForm';
import RegistrationForm from './RegistrationForm';

function App() {
    const [activeForm, setActiveForm] = useState('login');

    const showForm = (form) => {
        setActiveForm(form);
    };

    return (
        <div className="App">
            <nav>
                <button onClick={() => showForm('login')}>Login</button>
                <button onClick={() => showForm('register')}>Register</button>
            </nav>
            <div className="form-container">
                {activeForm === 'login' ? <LoginForm /> : <RegistrationForm />}
            </div>
        </div>
    );
}

export default App;