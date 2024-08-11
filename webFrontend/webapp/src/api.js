// src/api.js

const API_URL = 'http://localhost:8900/api';

export const getWeather = async (location) => {
  const res = await fetch(`${API_URL}/getWeather/${location}`);
  if (!res.ok) {
    throw new Error('No response received from backend');
  }
  return res.json();
};

export const sendWeather = async (data) => {
  const res = await fetch(`${API_URL}/sendWeather`, {
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
