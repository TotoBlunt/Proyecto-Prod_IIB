import socket
import urllib.request
import requests
import streamlit as st

def obtener_IPpublica():
    ip = requests.get("https://api.ipify.org").text 
    return ip

def geolocalizar_ip(ip):
    # Usar ipinfo.io para obtener la ubicación
    st.write(ip)
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("city", "Desconocida")
    return "Desconocida"
