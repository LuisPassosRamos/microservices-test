from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL do serviço de banco de dados
DB_SERVICE_URL = 'http://localhost:5001/users'

# Endpoint para listar usuários
@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get(DB_SERVICE_URL)
    print(response.json()) 
    return jsonify(response.json())

# Endpoint para adicionar um usuário
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    response = requests.post(DB_SERVICE_URL, json=new_user)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=5000)  # Executa na porta 5000
