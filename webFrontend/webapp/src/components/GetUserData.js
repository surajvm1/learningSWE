import React, { useState } from 'react';
import axios from 'axios';
import './GetUserData.css';

function GetUserData() {
  const [username, setUsername] = useState(''); // useState is a Hook in React that allows you to add state management to functional components. When you call useState, you pass the initial state as an argument, and it returns an array with two elements: The current state value, A function to update the state. Eg: const [count, setCount] = useState(0) - This line declares a state variable named count and initializes it to 0. setCount is a function that you can use to update the value of count.
  const [age, setAge] = useState('');
  const [data, setData] = useState(null);
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault(); // The preventDefault() method cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur. For example, this can be useful when: Clicking on a "Submit" button, prevent it from submitting a form. In my case, if I comment it and get data, the inputs go empty though at this point I have not designed tha backend
    setSuccessMessage('');
    setErrorMessage('');
    try {
      const response = await axios.get('http://localhost:8900/api/getUserData', {
        params: { username, age }
      });
      setData(response.data);
      setSuccessMessage('Data retrieved successfully!');
    } catch (error) {
      setErrorMessage('There was an error fetching the data.');
    }
  };

  return (
    <div className="container">
      <h1>Get User Data</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="age">Age:</label>
          <input
            type="number"
            id="age"
            value={age}
            onChange={(e) => setAge(e.target.value)}
            required
          />
        </div>
        <button type="submit">Get Data</button>
      </form>
      {successMessage && <p className="success">{successMessage}</p>}
      {errorMessage && <p className="error">{errorMessage}</p>}
      {data && (
        <div className="card">
          <h2>User Data</h2>
          <p><strong>Username:</strong> {data.username}</p>
          <p><strong>Age:</strong> {data.age}</p>
          <p><strong>Details:</strong> {data.details}</p>
        </div>
      )}
    </div>
  );
}

export default GetUserData;
