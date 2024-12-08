from supabase import create_client
import toml
import os

#Se realizo al creacion de secrets en github y streamlit para la gestion de credenciales de supabase
def get_supabase_credentials():
    """Obtiene las credenciales de Supabase desde las variables de entorno."""
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    if not supabase_url or not supabase_key:
        raise ValueError("Las credenciales de Supabase no están configuradas.")

    return supabase_url, supabase_key
supabase_url, supabase_key = get_supabase_credentials()
#obtener credenciales

def crear_cliente():
    return create_client(supabase_url,supabase_key)



