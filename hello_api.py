from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
    if request.method == 'GET':
        data = {"data": "Hello World"}
        return jsonify(data)


@app.route('/info', methods=['GET'])
def personaldata():
    if request.method == 'GET':
        details = {"name": "savanth", "profession": "developer", "mail id": "savanthks13055@gmail.com"}
        for detail in details:
            return jsonify(detail)


if __name__ == '__main__':
    app.run(debug=True)
