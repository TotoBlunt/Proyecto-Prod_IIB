from supabase_connector import inicializar_supabase
import os
import streamlit as st
import json


client = inicializar_supabase()

def crear_prediccion(predicction_data):
    st.subheader('Ingresar registro')
    try:
        datos = json.dumps(predicction_data,indent=4)
        # Insertar datos en Supabase
        response = client.table('datos_predicciones').insert(datos).execute()

        # Mostrar la respuesta completa para depuración
        st.write("Respuesta de Supabase:", response)

        if response.data:
            st.success('Registro creado con éxito')
        elif response.error:
            st.error(f"Error al crear el registro: {response.error}")
        elif hasattr(response, 'error') and response.error:
            print("Error en la consulta:", response.error)
        else:
            st.error("Respuesta inesperada de Supabase")
        
    except Exception as e:
        st.error(f"Error inesperado: {e}")  
   
    

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