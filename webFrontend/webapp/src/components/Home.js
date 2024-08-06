// src/components/Home.js

import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="container">
      <h1>Welcome to the User Service App</h1>
      <div>
        <Link to="/getUserData" className="link-button">Get User Data</Link>
        <Link to="/postUserData" className="link-button">Post User Data</Link>
        <Link to="/todayWeather" className="link-button">Today Weather</Link>
      </div>
    </div>
  );
}

export default Home;
