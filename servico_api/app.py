from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL do serviço de banco de dados
DB_URL = "http://localhost:5001/users"

# Endpoint GET /users (Consome o serviço de banco)
@app.route("/users", methods=["GET"])
def get_users():
    response = requests.get(DB_URL)
    return response.json(), response.status_code

# Endpoint POST /users (Consome o serviço de banco)
@app.route("/users", methods=["POST"])
def add_user():
    user = request.json
    response = requests.post(DB_URL, json=user)
    return response.json(), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
