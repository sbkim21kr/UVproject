import streamlit as st
import requests

api_base_url = "http://127.0.0.1:8000"

# GET image from FastAPI root
if st.button("Fetch Data"):
    response = requests.get(f"{api_base_url}/")
    json_data = response.json()
    st.image(json_data["Hello"])

# Sample item to send
item_data = {
    "name": "Seattle Supersonics",
    "description": "NBA team",
    "price": 10000,
    "tax": 100
}

# POST sample item
if st.button("Send Data"):
    response = requests.post(f"{api_base_url}/items/", json=item_data)
    st.json(response.json())

# Input for item ID
item_id = st.text_input("Enter Item ID")
target_url = f"{api_base_url}/items/{item_id}"

# READ item by ID
if st.button("READ"):
    response = requests.get(target_url)
    st.json(response.json())

# CREATE new item
if st.button("CREATE"):
    response = requests.post(
        f"{api_base_url}/items/",
        json={
            "name": "New Item",
            "description": "Created via Streamlit",
            "price": 5000,
            "tax": 500
        }
    )
    st.write(response.json())

# UPDATE item by ID
if st.button("PUT"):
    response = requests.put(
        target_url,
        json={
            "name": "Updated Item",
            "description": "Updated via Streamlit",
            "price": 111111111,
            "tax": 0
        }
    )
    st.write(response.json())

# DELETE item by ID
if st.button("DELETE"):
    response = requests.delete(target_url)
    st.write(response.json())


# Your FastAPI backend uses an in-memory dictionary called db to store items. 
# Each item gets a unique ID assigned automatically.