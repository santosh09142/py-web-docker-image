from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Python Web App Running Successfully"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()

    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)

    return jsonify({
        "result": num1 + num2
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)