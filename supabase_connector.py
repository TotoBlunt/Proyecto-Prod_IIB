from supabase import create_client
import toml
import os
import streamlit as st
#Se realizo al creacion de secrets en github y streamlit para la gestion de credenciales de supabase
def inicializar_supabase():
    
    """Obtiene las credenciales de Supabase desde las variables de entorno."""
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    client = create_client(url, key)
    return client
    


