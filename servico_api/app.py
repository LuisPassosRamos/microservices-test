from flask import Flask, request

import requests


app = Flask(__name__)

DB_URL = "http://servico_db:5001/users"

@app.route("/users", methods=["GET"])
def get_users():
    response = requests.get(DB_URL)
    return response.json(), response.status_code

@app.route("/users", methods=["POST"])
def add_user():
    user = request.json
    response = requests.post(DB_URL, json=user)
    return response.json(), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
