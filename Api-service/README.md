# Wine Quality Prediction Api Service
This project involves building a Flask web application for predicting the quality of wine using a pre-trained TensorFlow model. The application has four main files:

1. ### application.py
This file contains the Flask application responsible for handling HTTP requests and responses. It defines routes for predicting wine quality, retrieving all requests, and deleting all requests. The main functionalities include initializing the database, preprocessing input data, making predictions, saving requests to the database, and handling errors.

2. ### db_service.py
The db_service.py file provides functionalities related to the SQLite database used to store wine quality prediction requests. It includes methods for initializing the database, saving requests to the database, loading all requests, and deleting all requests.

3. ### ml_service.py
The ml_service.py file focuses on machine learning aspects. It contains functions for initializing a pre-trained TensorFlow model for wine quality prediction and making predictions using the model. The file also demonstrates example usage.

4. ### WineData.py
The WineData.py file defines a WineData class responsible for processing and handling input data for the wine prediction model. It includes methods for initializing attributes based on input data, creating a 2D array representation of the wine data, and retrieving the value of a specified attribute.

## How to Run
Install the required dependencies using the following command:

**pip install flask flask-cors tensorflow**

Run the Flask application using the following command:

**python application.py**

Access the API endpoints:

Predict Wine Quality: Send a POST request to /wine_quality with JSON data containing wine attributes.
Get All Requests: Send a GET request to /wine_quality to retrieve all stored requests.
Delete All Requests: Send a DELETE request to /wine_quality to delete all stored requests.
## Dependencies
1)Flask

2)Flask-CORS

3)TensorFlow

## Note

Ensure that the required model file (model-document) is available for the ml_service.py file to load the pre-trained model successfully.
