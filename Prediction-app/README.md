# Wine Quality Prediction Training model
This project involves building a machine learning model to predict the quality of white wine based on various features. The dataset used for training and evaluation is stored in the *Wine_quality_dataset* directory in the file named *winequality-white.csv*.

## Files

1. ### main.py

This script is the main entry point for the project. It imports the necessary modules, reads the dataset using downloading_data.py, splits the data into training and validation sets, builds a simple neural network using TensorFlow/Keras, compiles the model, trains it, and evaluates its performance.

2. ### downloading_data.py

This module is responsible for reading and processing the wine quality dataset. It uses the Pandas library to load the CSV file and converts the data into a suitable format for machine learning. The data is split into input features (x), corresponding labels (y), the number of data points (nw), and the number of features (n).
