import socket
import urllib.request
import requests
import streamlit as st

def obtener_IPpublica():
    ip = requests.get("https://api.ipify.org").text 
    return ip

def geolocalizar_ip():
    js_code = """
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(
    (position) => {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
      document.getElementById('location').innerText = `Tu ubicación es: Lat ${latitude}, Long ${longitude}`;
    },
    (error) => {
      console.error('Error al obtener la ubicación:', error);
      document.getElementById('location').innerText = 'No se pudo obtener la ubicación.';
    }
  );
} else {
  document.getElementById('location').innerText = 'Geolocalización no es soportada por este navegador.';
}
"""

    # Mostrar la ubicación en Streamlit
    st.write(f'<div id="location">Obteniendo ubicación...</div><script>{js_code}</script>', unsafe_allow_html=True)


'''

    # Usar ipinfo.io para obtener la ubicación
    st.write(ip)
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("city", "Desconocida")
    return "Desconocida"
'''