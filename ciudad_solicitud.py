import socket
import urllib.request

def obtener_IPpublica():
    ip_public = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return ip_public

def geolocalizar_ip(ip_public):
    # URL de la API de ipinfo.io con la IP publica específica
    url = f"https://ipinfo.io/{ip}/json"
    
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
        print(f"Error al conectarse a la API: {e}")
