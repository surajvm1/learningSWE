// src/components/TodayWeather.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TodayWeather() {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    const fetchWeather = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/todayWeather');
        setWeather(response.data);
      } catch (error) {
        console.error('There was an error fetching the weather data!', error);
      }
    };

    fetchWeather();
  }, []);

  return (
    <div className="container">
      <h1>Today Weather</h1>
      {weather ? (
        <div>
          <h2>Temperature is: {weather.temperature}</h2>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default TodayWeather;
