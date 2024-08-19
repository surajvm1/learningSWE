// src/api.js

const API_URL_POST_CALL = 'http://localhost:8765/api'; // Create/Post API call via Nginx and Kong

const API_URL = API_URL_POST_CALL // 'http://localhost:8900/api'; // Read, Update, Delete API directly with backend services, as Kong only supports POST API call load balancing and API gateway logic

export const getWeather = async (location) => {
  const res = await fetch(`${API_URL}/getWeather/${location}`);
  if (!res.ok) {
    throw new Error('No response received from backend');
  }
  return res.json();
};

export const sendWeather = async (data) => {
  const res = await fetch(`${API_URL_POST_CALL}/sendWeather`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    throw new Error('No response received from backend');
  }
  return res.json();
};

export const updateWeather = async (location, data) => {
  const res = await fetch(`${API_URL}/updateWeather/${location}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    throw new Error('No response received from backend');
  }
  return res.json();
};

export const deleteWeather = async (location) => {
  const res = await fetch(`${API_URL}/deleteWeather/${location}`, {
    method: 'DELETE',
  });
  if (!res.ok) {
    throw new Error('No response received from backend');
  }
  return res.json();
};
