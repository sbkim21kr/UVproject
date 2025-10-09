import requests

data = {
    "name": "Seattle Supersonics",
    "description": "NBA team",
    "price": 10000,
    "tax": 20
}

response = requests.post(
    "http://127.0.0.1:8500/items/", 
    json=data)

print(response.json())
