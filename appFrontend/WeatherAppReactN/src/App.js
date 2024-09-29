// App.js

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import HomeScreen from './components/HomeScreen';
import GetWeatherData from './components/GetWeatherData';
import SendWeatherData from './components/SendWeatherData';
import UpdateWeatherData from './components/UpdateWeatherData';
import DeleteWeatherData from './components/DeleteWeatherData';

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="GetWeather" component={GetWeatherData} />
        <Stack.Screen name="SendWeather" component={SendWeatherData} />
        <Stack.Screen name="UpdateWeather" component={UpdateWeatherData} />
        <Stack.Screen name="DeleteWeather" component={DeleteWeatherData} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;