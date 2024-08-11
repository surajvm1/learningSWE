import React, { useState } from 'react';
import { updateWeather } from '../api';

function UpdateWeatherData() {
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
      const result = await updateWeather(location, data);
      setResponse(result);
    } catch (error) {
      setResponse({ error: error.message || 'Failed to update weather data.' });
    }
  };

  return (
    <div>
      <h2>Update Local Weather Data</h2>
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
        <button type="submit">Update Data</button>
      </form>
      {response && (
        <div className="card">
          {response.error ? (
            <p className="error">{response.error}</p>
          ) : (
            <p>Weather data updated successfully!</p>
          )}
        </div>
      )}
    </div>
  );
}

export default UpdateWeatherData;
