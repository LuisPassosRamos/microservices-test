from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

FILE_PATH = "users.json"

def read_users():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []

def write_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)

@app.route("/users", methods=["GET"])
def get_users():
    users = read_users()
    return jsonify(users), 200

@app.route("/users", methods=["POST"])
def add_user():
    user = request.json
    users = read_users()
    users.append(user)
    write_users(users)
    return jsonify({"message": "User added successfully!"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
