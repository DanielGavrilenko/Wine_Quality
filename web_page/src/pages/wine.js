// pages/wine.js

import React, { useState } from 'react';
import axios from 'axios';
import Head from 'next/head';
import '../../styles/styles.css';

const WineInputField = ({ label, name, value, onChange }) => (
  <tr>
    <th scope="row">{label}</th>
    <td><input type="text" name={name} value={value} onChange={onChange} /></td>
  </tr>
);

const Wine = () => {
  const [wineData, setWineData] = useState({/* ... (unchanged) */});
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setWineData({ ...wineData, [name]: value });
};

const handleFetchData = async () => {
    try {
      setLoading(true);
      const response = await axios.post('http://127.0.0.1:5000/wine_quality', wineData);
      setResult(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
      setError('An error occurred while fetching data.');
    } finally {
      setLoading(false);
    }
};

  return (
    <div>
      <h1>Wine Quality Page</h1>

      <Head>
      <title>Your Webpage</title>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      </Head>

      <div className="background"></div>
      <div className="content">
      </div>
        
      <table>
        <thead>
          <tr>
            <th>Parameters</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          <tr>
              <td scope="row">Fixed Acidity</td>
              <td><input type="text" name="fixed_acidity" value={wineData.fixed_acidity} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>Volatile Acidity</td>
              <td><input type="text" name="volatile_acidity" value={wineData.volatile_acidity} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>Citric Acid</td>
              <td><input type="text" name="citric_acid" value={wineData.citric_acid} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>Residual Sugar</td>
              <td><input type="text" name="residual_sugar" value={wineData.residual_sugar} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>Chlorides</td>
              <td><input type="text" name="chlorides" value={wineData.chlorides} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>Free Sulfur Dioxide</td>
              <td><input type="text" name="free_sulfur_dioxide" value={wineData.free_sulfur_dioxide} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>Total Sulfur Dioxide</td>
              <td><input type="text" name="total_sulfur_dioxide" value={wineData.total_sulfur_dioxide} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>Density</td>
              <td><input type="text" name="density" value={wineData.density} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>PH</td>
              <td><input type="text" name="pH" value={wineData.pH} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>Sulphates:PH</td>
              <td><input type="text" name="sulphates" value={wineData.sulphates} onChange={handleInputChange} /></td>
            </tr>
            <tr>
              <td>Alcohol</td>
              <td><input type="text" name="alcohol" value={wineData.alcohol} onChange={handleInputChange} /></td>
            </tr>
        </tbody>
      </table>

      <button onClick={handleFetchData} disabled={loading}>
        {loading ? 'Fetching Data...' : 'Fetch Wine Quality'}
      </button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {result && (
        <div>
          <h2>Result:</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default Wine;
