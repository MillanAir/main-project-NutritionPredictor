from flask import Flask, jsonify, request
from joblib import load
from flask_cors import CORS

model = load("../models/nutrition_model_decisiontree_gridsearch.pkl")

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    ingredients = [data.get('ingredients')]

    prediction = model.predict(ingredients)

    output = {
        'calories': prediction[0][0],
        'carbs': prediction[0][1],
        'proteins': prediction[0][2],
        'fats': prediction[0][3],
    }
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)