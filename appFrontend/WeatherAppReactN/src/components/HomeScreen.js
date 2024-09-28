// src/components/HomeScreen.js

import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Weather Data Management</Text>
      <Button title="Get Weather of a City" onPress={() => navigation.navigate('GetWeather')} />
      <Button title="Send Local Weather Data" onPress={() => navigation.navigate('SendWeather')} />
      <Button title="Update Local Weather Data" onPress={() => navigation.navigate('UpdateWeather')} />
      <Button title="Delete Local Weather Data" onPress={() => navigation.navigate('DeleteWeather')} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f6d365',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
});

export default HomeScreen;