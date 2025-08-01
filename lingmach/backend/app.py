from flask import Flask, request, jsonify
from flask_cors import CORS
from generator import generate_text

app = Flask(__name__)
CORS(app)  

@app.route('/', methods=['GET'])
def home():
    return "flask is running!"

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'GET':
        return "Send a POST request with JSON"

    data = request.get_json()
    prompt = data.get('prompt', '')
    result = generate_text(prompt)
    return jsonify({'generated': result})

if __name__ == '__main__':
    app.run(debug=True)
