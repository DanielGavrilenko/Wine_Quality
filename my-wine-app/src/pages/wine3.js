import { useState } from 'react';
import React from 'react';
import axios from 'axios';
//import '../../styles/styles.css';

export default function Wine() {
  const [wineData, setWineData] = useState({
    // ... (unchanged)
  });

  const [result, setResult] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setWineData({ ...wineData, [name]: value });
  };

  const handleFetchData = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/wine_quality', wineData);
      setResult(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
      setResult(null);
    }
  };

  return (
    <div>
      <h1>Wine Quality Page</h1>

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


      <button onClick={handleFetchData}>Fetch Wine Quality</button>

      {result && (
        <div>
          <h2>Result:</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
