import requests

url = "http://localhost:5001/users"  # Endpoint do serviço de banco de dados
data = {
    "id": 1,
    "name": "João",
    "email": "joao@email.com"
}

# Adicione o cabeçalho Content-Type
response = requests.post(url, json=data, headers={"Content-Type": "application/json"})

# Exibe a resposta do servidor
print(response.json())
