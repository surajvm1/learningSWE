// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import GetWeatherData from './components/GetWeatherData';
import SendWeatherData from './components/SendWeatherData';
import UpdateWeatherData from './components/UpdateWeatherData';
import DeleteWeatherData from './components/DeleteWeatherData';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Weather Data Management</h1>
        <Routes>
          <Route
            path="/"
            element={
              <div className="home">
                <h2>Choose an Option</h2>
                <div className="button-container">
                  <Link to="/get-weather" className="button">Get Weather of a City</Link>
                  <Link to="/send-weather" className="button">Send Local Weather Data</Link>
                  <Link to="/update-weather" className="button">Update Local Weather Data</Link>
                  <Link to="/delete-weather" className="button">Delete Local Weather Data</Link>
                </div>
              </div>
            }
          />
          <Route path="/get-weather" element={<GetWeatherData />} />
          <Route path="/send-weather" element={<SendWeatherData />} />
          <Route path="/update-weather" element={<UpdateWeatherData />} />
          <Route path="/delete-weather" element={<DeleteWeatherData />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
