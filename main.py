from flask import Flask, request, jsonify
from line import pred_line

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/predict', methods=['POST'])
def predict():
    team_name = request.json.get('team_name')
    location = request.json.get('location')
    try:
        predictions = pred_line(team_name, location)
        return jsonify(predictions)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
