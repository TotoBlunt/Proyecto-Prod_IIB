from supabase import create_client
import toml
import os

#Se realizo al creacion de secrets en github y streamlit para la gestion de credenciales de supabase
def inicializador_supabase():
    """Obtiene las credenciales de Supabase desde las variables de entorno."""
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    if not supabase_url or not supabase_key:
        raise ValueError("Las credenciales de Supabase no están configuradas.")

    return create_client(supabase_url,supabase_key)


try:
    client = inicializar_supabase()
    st.write("Conexión a Supabase verificada")
except Exception as e:
    st.error(f"Error conectando a Supabase: {e}")
    raise

