// src/components/PostUserData.js

import React, { useState } from 'react';
import axios from 'axios';

function PostUserData() {
  const [username, setUsername] = useState('');
  const [age, setAge] = useState('');
  const [location, setLocation] = useState('');
  const [email, setEmail] = useState('');
  const [response, setResponse] = useState(null);
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSuccessMessage('');
    setErrorMessage('');
    try {
      const res = await axios.post('http://localhost:5000/api/postUserData', { username, age, location, email });
      setResponse(res.data);
      setSuccessMessage('Data posted successfully!');
    } catch (error) {
      setErrorMessage('There was an error posting the data.');
    }
  };

  return (
    <div className="container">
      <h1>Post User Data</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="age">Age:</label>
          <input
            type="number"
            id="age"
            value={age}
            onChange={(e) => setAge(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="location">Location (optional):</label>
          <input
            type="text"
            id="location"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <button type="submit">Post Data</button>
      </form>
      {successMessage && <p className="success">{successMessage}</p>}
      {errorMessage && <p className="error">{errorMessage}</p>}
      {response && (
        <div>
          <h2>Response from Server</h2>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default PostUserData;
