// Import necessary modules
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Define your component
function MyComponent() {
  // State to store the data
  const [responseData, setResponseData] = useState(null);

  // useEffect to fetch data when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Make the Axios GET request
        const response = await axios.get('http://127.0.0.1:5000/wine_quality');

        // Set the response data in the state
        setResponseData(response.data);
      } catch (error) {
        // Handle errors
        console.error('Error during Axios request:', error);
      }
    };

    // Call the fetchData function
    fetchData();
  }, []); // Empty dependency array means this effect runs once when the component mounts

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Fixed Acidity</th>
            <th>Volatile Acidity</th>
            <th>Citric Acid</th>
            <th>Residual Sugar</th>
            <th>Chlorides</th>
            <th>Free Sulfur Dioxide</th>
            <th>Total Sulfur Dioxide</th>
            <th>Density</th>
            <th>PH</th>
            <th>Sulphates</th>
            <th>Alcohol</th>
            <th>Prediction</th>
            {/* Add more columns as needed */}
          </tr>
        </thead>
        <tbody>
          {responseData && responseData.output.map((row, index) => (
            <tr key={index}>
              {row.map((cell, cellIndex) => (
                <td key={cellIndex}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

// Export your component
export default MyComponent;
