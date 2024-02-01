# Node.js Wine Quality Prediction Project
This Node.js project consists of two pages, wine.js and database_records.js, aimed at predicting wine quality based on user-input parameters and displaying the records stored in the database.

## wine.js
### Description
The wine.js page allows users to input various parameters related to wine quality and predicts the outcome using a machine learning model. Additionally, it provides an option to fetch previous records from the database.

### Features

1) Input fields for parameters such as fixed acidity, volatile acidity, citric acid, etc.
2) Predict button to trigger the prediction process.
3) Fetch Data from Database button to retrieve previous records.
4) Dynamic rendering of the prediction result.
5) Error handling for data fetching.

### Usage

1) Enter the wine parameters in the respective input fields.
2) Click the "Predicting" button to initiate the prediction process.
3) Optionally, click the "Fetch Data from database about previous records" button to retrieve stored records.
4) View the prediction result and any potential errors.

### Code Overview

*WineInputField Component*: A reusable component for rendering input fields.

*State Management*: Utilizes React hooks for state management.

*Data Fetching*: Axios is used to send requests to the server for prediction and database records.

*New Window*: Opens a new browser window/tab to display database records.

## database_records.js

### Description

The database_records.js page retrieves and displays records stored in the database related to wine quality predictions. It uses Axios to fetch data when the component mounts.

### Features
1) Displays a table with columns for various parameters and prediction results.
2) Utilizes React hooks and useEffect for efficient data fetching.

### Usage

The component automatically fetches and displays the records when mounted.

### Code Overview

*MyComponent*: The main component that fetches and displays records. 

*State Management*: Uses React hooks for state management.

*Data Fetching*: Axios is used to retrieve data from the server.

*Table Rendering*: Dynamically renders the records in a table format.

### Setup
1) Clone the repository.
2) Install dependencies using npm install.
3) Run the application using npm start.
### Dependencies

React

Axios

### Note
Make sure the server (http://127.0.0.1:5000) is running for both prediction and data fetching functionalities.

Feel free to customize and extend the project as needed for your specific requirements.
