from supabase_connector import crear_cliente
import os
import streamlit as st

client = crear_cliente()


def crear_prediccion(predicction_data):
    st.subheader('Ingresar registro')
    # Verificar que predicction_data contenga los datos necesarios
    required_keys = ['feature_3', 'feature_1', 'feature_2', 'feature_4', 'feature_5', 'created_at']
    for key in required_keys:
        if key not in predicction_data:
            st.error(f"Falta la clave '{key}' en predicction_data")
            return
    
    # Crear el diccionario de datos a insertar
    data = {
        'peso_sem3': predicction_data['feature_3'],
        'peso_sem4': predicction_data['feature_1'],
        'agua': predicction_data['feature_2'],
        'consumo_acabado': predicction_data['feature_4'],
        'mortalidad_std': predicction_data['feature_5'],
        'created_at': predicction_data['created_at']
    }
    
    try:
        # Insertar datos en Supabase
        response = client.table('datos_predicciones').insert(data).execute()
        
        # Verificar la respuesta de Supabase
        if response.get('status_code') == 201:
            st.success('Registro Creado con Éxito')
        else:
            st.error(f"Error al crear el registro: {response.get('message')}")
    
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