// src/components/UpdateWeatherData.js

import React, { useState } from 'react';
import { View, TextInput, Button, Text, StyleSheet } from 'react-native';
import { updateWeather } from '../api'; // Adjust the path as needed

function UpdateWeatherData() {
  const [user, setUser] = useState('');
  const [location, setLocation] = useState('');
  const [temperature, setTemperature] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async () => {
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
    <View>
      <TextInput placeholder="User" value={user} onChangeText={setUser} />
      <TextInput placeholder="Location" value={location} onChangeText={setLocation} />