// src/components/GetUserData.js

import React, { useState } from 'react';
import axios from 'axios';

function GetUserData() {
  const [username, setUsername] = useState('');
  const [age, setAge] = useState('');
  const [data, setData] = useState(null);

// useState is a Hook in React that allows you to add state management to functional components. When you call useState, you pass the initial state as an argument, and it returns an array with two elements: The current state value, A function to update the state. Eg: const [count, setCount] = useState(0) - This line declares a state variable named count and initializes it to 0. setCount is a function that you can use to update the value of count.

  const handleSubmit = async (e) => {
    e.preventDefault(); // The preventDefault() method cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur. For example, this can be useful when: Clicking on a "Submit" button, prevent it from submitting a form. In my case, if I comment it and get data, the inputs go empty though at this point I have not designed tha backend
    try {
      const response = await axios.get(`http://localhost:5000/api/getUserData`, {
        params: { username, age }
      });
      setData(response.data);
    } catch (error) {
      console.error('There was an error fetching the data!', error);
    }
  };

  return (
    <div className="container">
      <h1>Get User Data</h1>
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
        <button type="submit">Get Data</button>
      </form>
      {data && (
        <div>
          <h2>Data from Server</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
          {/* Comment: {JSON.stringify(data, null, 2)}: JSON.stringify is a method in JavaScript that converts a JavaScript object or value to a JSON string. The first parameter (data) is the JavaScript object you want to convert to a JSON string. The second parameter (null) is used for a replacer function, which allows you to alter the behavior of the stringification process (in this case, it is null, meaning no alteration). The third parameter (2) is the number of spaces to use as white space for indentation in the output JSON string. This makes the JSON string more readable by adding line breaks and indentation. */}
        </div>
      )}
    </div>
  );
}

export default GetUserData;
