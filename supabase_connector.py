from supabase import create_client
import pandas as pd
import os

def get_supabase_credentials():
    """Obtiene las credenciales de Supabase desde las variables de entorno."""
    supabase_url = os.environ.get('SUPABASE_URL')
    supabase_key = os.environ.get('SUPABASE_KEY')

    if not supabase_url or not supabase_key:
        raise ValueError("Las credenciales de Supabase no están configuradas.")

    return supabase_url, supabase_key

#obtener credenciales
supabase_url, supabase_key = get_supabase_credentials()

supabase: Client = create_client(supabase_url,supabase_key)


