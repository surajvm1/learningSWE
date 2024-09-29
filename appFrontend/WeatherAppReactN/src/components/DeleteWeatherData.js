// src/components/DeleteWeatherData.js

import React, { useState } from 'react';
import { View, TextInput, Button, Text } from 'react-native';
import { deleteWeather } from '../api'; // Adjust the path as needed

function DeleteWeatherData() {
  const [location, setLocation] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async () => {
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
    <View>
      <TextInput
        placeholder="Location"
        value={location}
        onChangeText={setLocation}
      />
      <Button title="Delete Data" onPress={handleSubmit} />
      {response && (
        <Text>{response.error ? response.error : 'Weather data deleted successfully!'}</Text>
      )}
    </View>
  );
}

export default DeleteWeatherData;