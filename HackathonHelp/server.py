from flask import Flask, request, jsonify, send_from_directory
import os
from prima import count_characters  # Import the function from prima.py

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/script.js')
def serve_js():
    return send_from_directory('.', 'script.js')

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    input_string = data.get('data', '')
    character_count = count_characters(input_string)
    result = {'output': f'The number of characters in the input is: {character_count}'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
