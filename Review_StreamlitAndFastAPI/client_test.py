import requests

response = requests.get("http://127.0.0.1:8000/")
print(response.json())


# This code is acting like a client — just like a browser, mobile app, or frontend 
# — sending a request to your FastAPI server and reading the response.

# It’s useful for:

#     ✅ Testing your API without using Swagger UI (/docs)

#     ✅ Automating requests (e.g., for scripts, bots, or monitoring)

#     ✅ Simulating real-world usage from another system

#     ✅ Debugging how your server responds to different inputs


# 🧩 Why open a separate terminal?

# Because:

#     Your FastAPI server is already running in one terminal (via uvicorn)

#     You need a second process to act as the client

# It’s like having one window for the restaurant kitchen (server) 
# and another for the customer placing an order (client).