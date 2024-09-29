// src/components/SendWeatherData.js

import React, { useState } from 'react';
import { View, TextInput, Button, Text } from 'react-native';
import { sendWeather } from '../api';

function SendWeatherData() {
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
      const result = await sendWeather(data);
      setResponse(result);
    } catch (error) {
      setResponse({ error: error.message || 'Failed to send weather data.' });
    }
  };

  return (
    <View>
      <TextInput placeholder="User" value={user} onChangeText={setUser} />
      <TextInput placeholder="Location" value={location} onChangeText={setLocation} />
      <TextInput placeholder="Temperature (integer)" value={temperature} onChangeText={setTemperature} keyboardType="numeric" />
      <Button title="Send Data" onPress={handleSubmit} />
      {response && (
        <Text>{response.error ? response.error : 'Weather data sent successfully!'}</Text>
      )}
    </View>
  );
}

export default SendWeatherData;