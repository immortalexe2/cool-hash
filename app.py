from flask import Flask, render_template, request, jsonify
import hashlib

app = Flask(__name__)

hash_algorithms = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
    'sha512': hashlib.sha512,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash', methods=['POST'])
def hash_text():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    input_text = data.get('inputText', '')
    hash_type = data.get('hashType', '').lower()

    if hash_type not in hash_algorithms:
        return jsonify({'error': 'Unsupported hash type'}), 400

    hash_func = hash_algorithms[hash_type]
    hashed = hash_func(input_text.encode()).hexdigest()

    return jsonify({'hashed': hashed})

if __name__ == '__main__':
    app.run(debug=True)