import React, { useState } from 'react';
import { getWeather } from '../api';

function GetWeatherData() {
  const [location, setLocation] = useState('');
  const [temperature, setTemperature] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!location) {
      setError('Location is required.');
      return;
    }

    try {
      const result = await getWeather(location);
      setTemperature(result.temperature);
      setError(null);
    } catch (error) {
      setTemperature(null);
      setError(error.message || 'Failed to get weather data.');
    }
  };

  return (
    <div>
      <h2>Get Weather Data</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
        <button type="submit">Get Data</button>
      </form>
      {temperature && (
        <div className="card">
          <p>Location: {location}</p>
          <p>Temperature: {temperature}°C</p>
        </div>
      )}
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default GetWeatherData;
