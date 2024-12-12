from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Caminho do arquivo JSON
JSON_FILE = 'users.json'

# Função para carregar usuários
def load_users():
    try:
        with open(JSON_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Função para salvar usuários
def save_users(users):
    with open(JSON_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# Endpoint para retornar todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    users = load_users()
    return jsonify(users)

# Endpoint para adicionar um novo usuário
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    if not new_user.get("id") or not new_user.get("name") or not new_user.get("email"):
        return jsonify({"error": "Missing fields"}), 400
    users = load_users()
    users.append(new_user)
    save_users(users)
    return jsonify({"message": "User added successfully!"}), 201

if __name__ == '__main__':
    app.run(port=5001)  # Executa na porta 5001