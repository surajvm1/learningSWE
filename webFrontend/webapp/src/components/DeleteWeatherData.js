import React, { useState } from 'react';
import { deleteWeather } from '../api';

function DeleteWeatherData() {
  const [location, setLocation] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!location) {
      setResponse({ error: 'Location is required.' });
      return;
    }

    try {
      const result = await deleteWeather(location);
      setResponse(result);
    } catch (error) {
      setResponse({ error: error.message || 'Failed to delete weather data.' });
    }
  };

  return (
    <div>
      <h2>Delete Local Weather Data</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
        <button type="submit">Delete Data</button>
      </form>
      {response && (
        <div className="card">
          {response.error ? (
            <p className="error">{response.error}</p>
          ) : (
            <p>Weather data deleted successfully!</p>
          )}
        </div>
      )}
    </div>
  );
}

export default DeleteWeatherData;
