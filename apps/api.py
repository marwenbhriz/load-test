from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def my_api():
    data = {"message": "Hello, Load Test!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)