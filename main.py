from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
    if request.method == 'GET':
        data = {"data": "Hello World"}
        return jsonify(data)


@app.route('/info', methods=['GET'])
def personal_data():
    if request.method == 'GET':
        details = {"name": "savanth",
                   "profession": "developer",
                   "mail id": "savanthks13055@gmail.com"}
        return jsonify(details)


@app.route('/input', methods=['POST'])
def input():
    body = request.json
    return body


@app.route('/add', methods=['POST'])
def addition():
    numbers = request.json
    sum = 0
    for number in numbers['num']:
        sum = sum + number
    return str(sum)


if __name__ == '__main__':
    app.run(debug=True)
