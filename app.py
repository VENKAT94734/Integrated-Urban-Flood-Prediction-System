from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def predict_flood(rainfall, water_level):
    if rainfall > 80 and water_level > 7:
        return "High Risk"
    elif rainfall > 50 and water_level > 5:
        return "Moderate Risk"
    else:
        return "Low Risk"

@app.route('/')
def home():
    return "Flood Prediction API Running"

@app.route('/heatmap-data', methods=['GET'])
def heatmap():
    data = [
        {"lat": 17.3850, "lng": 78.4867, "risk": "High"},
        {"lat": 17.3950, "lng": 78.4767, "risk": "Moderate"},
        {"lat": 17.4050, "lng": 78.4667, "risk": "Low"},
        {"lat": 17.3750, "lng": 78.4967, "risk": "High"},
        {"lat": 17.3650, "lng": 78.5067, "risk": "Moderate"}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
