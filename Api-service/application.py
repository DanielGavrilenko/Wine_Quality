from flask import Flask, request, jsonify
# from openai import OpenAI
from WineData import WineData
import db_service as db
import ml_service as mod
from flask_cors import CORS
global wine_model


app = Flask(__name__)
CORS(app)


@app.route('/wine_quality', methods=['POST'])
def analyse_wine():
    try:
        db.init_db()
        # retrieve JSON data from the incoming request
        input_data = request.get_json()

        # Preprocess the received data for model input
        input_model_data = WineData(input_data)

        # Make a prediction using the processed data
        prediction = mod.predict_wine_quality(wine_model, input_model_data)

        # Save the input_model_data in the database
        db.save_request(input_model_data, prediction)

        # Return the prediction as a JSON response
        return jsonify({'Prediction: ': prediction})

    except Exception as e:
        # Handle exceptions and return an error message as a JSON response
        return jsonify({"error": str(e)}), 500


@app.route('/wine_quality', methods=['GET'])
def get_all_requests():
    try:
        data_db = db.load_requests()
        return jsonify({'output': data_db})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/wine_quality', methods=['DElETE'])
def delete_requests():
    try:
        db.delete_requests()
        return jsonify({'output': 'success'})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    db.init_db()
    wine_model = mod.init_model('model-document')
    app.run(debug=False)
