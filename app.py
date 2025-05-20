# app.py
from flask import Flask, request
from http import HTTPStatus
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    request_data = request.data.decode('utf-8')
    print("request data:", request_data)
    return request_data, HTTPStatus.OK

if __name__ == "__main__":
    app.run()
