import streamlit as st
import requests

response = requests.get("http://127.0.0.1:8000/")
# json으로 반환되는 데이터는 딕셔너리로 변환되어 있음.
# 따라서, Hello key의 value를 가져오면 됨
st.image(response.json()["Hello"])


# FastAPI acts as your backend — it serves data (like a dictionary with a key "Hello" and a value that’s an image URL).

# Streamlit acts as your frontend — it sends a request to FastAPI, receives the data, and displays it (in this case, an image).