// src/components/GetWeatherData.js

import React, { useState } from 'react';
import { View, TextInput, Button, Text, StyleSheet } from 'react-native';
import { getWeather } from '../api';

function GetWeatherData() {
  const [location, setLocation] = useState('');
  const [temperature, setTemperature] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
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
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Location"
        value={location}
        onChangeText={setLocation}
      />
      <Button title="Get Data" onPress={handleSubmit} />
      {temperature && <Text>Temperature: {temperature}°C</Text>}
      {error && <Text style={styles.error}>{error}</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 20,
    paddingHorizontal: 10,
  },
  error: {
    color: 'red',
    marginTop: 10,
  },
});

export default GetWeatherData;