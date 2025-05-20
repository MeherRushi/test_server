# app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    print("request data", request.data)
    return "Hello, HTTPS World!"

if __name__ == "__main__":
    app.run()
