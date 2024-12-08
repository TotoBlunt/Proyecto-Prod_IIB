from supabase import create_client
import os

#Se realizo al creacion de secrets en github para la gestion de credenciales de supabase
def get_supabase_credentials():
    """Obtiene las credenciales de Supabase desde las variables de entorno."""
    supabase_url = 'https://lxsxxgaudhliaoerewmp.supabase.co'
    supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx4c3h4Z2F1ZGhsaWFvZXJld21wIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzM2NjA1NjEsImV4cCI6MjA0OTIzNjU2MX0.F8y5gGcsx6e4TS-Ce1SIq0sbkEBuvLzmGr8qCPeq8rw'

    if not supabase_url or not supabase_key:
        raise ValueError("Las credenciales de Supabase no están configuradas.")

    return supabase_url, supabase_key

supabase_url, supabase_key = get_supabase_credentials()
#obtener credenciales

def crear_cliente():
    return create_client(supabase_url,supabase_key)


