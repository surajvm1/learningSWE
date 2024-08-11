import React, { useState } from 'react';
import { sendWeather } from '../api';

function SendWeatherData() {
  const [user, setUser] = useState('');
  const [location, setLocation] = useState('');
  const [temperature, setTemperature] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!user || !location || !temperature || isNaN(temperature)) {
      setResponse({ error: 'All fields are required and temperature must be an integer.' });
      return;
    }

    const data = { user, location, temperature: parseInt(temperature) };

    try {
      const result = await sendWeather(data);
      setResponse(result);
    } catch (error) {
      if (error.response && error.response.status === 400) {
        setResponse({ error: 'Location already exists. Please update the existing record.' });
      } else {
        setResponse({ error: error.message || 'Failed to send weather data.' });
      }
    }
  };

  return (
    <div>
      <h2>Send Local Weather Data</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="User"
          value={user}
          onChange={(e) => setUser(e.target.value)}
        />
        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
        <input
          type="number"
          placeholder="Temperature (integer)"
          value={temperature}
          onChange={(e) => setTemperature(e.target.value)}
        />
        <button type="submit">Send Data</button>
      </form>
      {response && (
        <div className="card">
          {response.error ? (
            <p className="error">{response.error}</p>
          ) : (
            <p>Weather data sent successfully!</p>
          )}
        </div>
      )}
    </div>
  );
}

export default SendWeatherData;
