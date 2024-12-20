import socket
import urllib.request
import requests
import streamlit as st

def obtener_IPpublica():
    ip_public = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return ip_public

def geolocalizar_ip():
    # URL de la API de ipinfo.io con la IP publica específica
    #url = f"https://ipinfo.io/{ip}/json"

    # Código JavaScript para obtener la ubicación del usuario
    js_code = """
    fetch('https://ipinfo.io/json')
    .then(response => response.json())
    .then(data => {
        document.getElementById('location').innerText = `Tu ubicación es: ${data.city}, ${data.country}`;
    })
    .catch(error => {
        console.error('Error al obtener la ubicación:', error);
        document.getElementById('location').innerText = 'No se pudo obtener la ubicación.';
    });
    """

    # Mostrar la ubicación en Streamlit
    st.write(f'<div id="location">Obteniendo ubicación...</div><script>{js_code}</script>', unsafe_allow_html=True)
    '''
    try:
        # Realizar la solicitud HTTP GET
        respuesta = requests.get(url)
        datos = respuesta.json()

        # Extraer información relevante
        ip = datos.get("ip")
        ciudad = datos.get("city")
        region = datos.get("region")
        pais = datos.get("country")
        coordenadas = datos.get("loc")  # Coordenadas en formato "lat,lon"

        return ciudad
        

    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse a la API: {e}")'''
