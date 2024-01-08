import tensorflow as tf
from WineData import WineData
'''
functions process tensorflow wine prediction model
'''


def init_model(model_path):
    """
    Load a pre-trained wine quality prediction model.

    Parameters:
    - model_path (str): The path to the saved TensorFlow model.

    Returns:
    - wine_model (tf.keras.Model): A loaded TensorFlow model for wine quality prediction.
    """
    wine_model = tf.keras.models.load_model(model_path)
    return wine_model


def predict_wine_quality(wine_model, data):
    """
    Make predictions using the provided wine_model on the given data.

    Parameters:
    - wine_model (tf.keras.Model): A trained TensorFlow model for wine quality prediction.
    - data (YourDataType): Input data for prediction.

    Returns:
    - prediction: The predicted wine quality.
    """
    # Ensure data is in the expected format before prediction
    if not isinstance(data, WineData):  # Replace YourDataType with the actual type
        raise ValueError("Invalid data type. Expected WineData.")

    prediction = wine_model.predict(data.get_2d_array())
    return prediction
# Example usage:
# model = initialising_model_model(r'F:\Pycharm projects\Wine quality\model_document')
# prediction = predict_wine_quality(model, your_data)
