import requests

url = "http://localhost:5000/users"  # Ajuste para a porta correta
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print("Response Body:")
print(response.text)
