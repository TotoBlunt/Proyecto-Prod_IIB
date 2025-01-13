from supabase_connector import inicializar_supabase
import os
import streamlit as st
import json
from supabase import create_client, Client

Client = inicializar_supabase()


def crear_prediccion(predicction_data):
    st.subheader('Ingresando registro...')
    try:
        # Mostrar los datos que se van a insertar (opcional)
        #st.write("## Datos a insertar:", json.dumps(predicction_data,indent=4))

        # Convertir el diccionario a JSON
        json_data = json.loads(predicction_data)  # json.dumps crea el formato correcto
        #st.write("Datos en formato JSON_loads:", json_data)

        # Insertar datos en Supabase
        response = Client.table('predicciones').insert(json_data).execute()

        # Mostrar la respuesta completa para depuración (opcional)
        #st.write("Respuesta de Supabase:", response)

        # Verificar si la operación fue exitosa
        if response.data:
            st.success('Registro creado con éxito')
        elif response.error:
            st.error(f"Error al crear el registro: {response.error}")
        else:
            st.error("Respuesta inesperada de Supabase")

    except Exception as e:
        st.error(f"Guardando....")

def verificar_registros():
    """Verifica si hay al menos un registro en la tabla 'datos_predicciones'."""
    try:
        response = Client.table('predicciones').select('*').limit(1).execute()
        return len(response.data) > 0
    except Exception as e:
        st.error(f"Ocurrió un error al verificar los registros: {e}")
        return False

def listar_registros():
    st.subheader('Listar todos los registros')
    try:
        # Obtener los datos de la tabla 'datos_predicciones'
        response = Client.table('predicciones').select('*').execute()
        
        # Verificar si la respuesta contiene datos
        if response.data:
            # Mostrar los datos en una tabla en Streamlit
            st.table(response.data)
        else:
            st.write("No hay registros para mostrar.")
    
    except Exception as e:
        st.error(f"Ocurrió un error al listar los registros: {e}")

def eliminar_prediccion(prediccion_id):
    """
    Elimina una predicción de la base de datos Supabase por su ID.
    
    :param prediccion_id: ID de la predicción a eliminar.
    :return: True si la eliminación fue exitosa, False en caso contrario.
    """
    try:
        # Eliminar el registro con el ID proporcionado
        supabase.table('predicciones').delete().eq('id', prediccion_id).execute()
        return True
    except Exception as e:
        print(f"Error al eliminar la predicción: {e}")
        return False
    
'''
def read_prediccion():
    st.subheader('Leer Registro')
    response = client.table('datos_predicciones').select('*').eq('id',prediction_id).execute()
    return response.data

def update_prediccion():
    st.subheader('Actualizar Registro')
    new_data = new_data
    response = client.table('datos_predicciones').update(new_data).eq('id',prediction_id).execute()
    return response

def delete_prediccion():
    st.subheader('Eliminar Registro')
    response = client.table('datos_predicciones').delete().eq('id',prediction_id).execute()
    return response

def listar_registros():
    st.subheader('Listar todos los registros')
    response = client.table('datos_predicciones').select('*').execute()

def main_menu():
    st.subheader("Menú CRUD con Streamlit y Supabase")
    menu = ["Crear Registro", "Leer Registro", "Actualizar Registro", "Eliminar Registro", "Listar Todos los Registros"]
    choice = st.sidebar.selectbox("Seleccione una opción", menu)
    
    if choice == "Crear Registro":
        crear_prediccion()
    elif choice == "Leer Registro":
        read_prediccion()
    elif choice == "Actualizar Registro":
        update_prediccion()
    elif choice == "Eliminar Registro":
        delete_prediccion()
    elif choice == "Listar Todos los Registros":
        listar_registros()
        '''