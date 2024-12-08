from supabase_connector import crear_cliente
import os
import streamlit as st
client = crear_cliente()


def crear_prediccion(predicction_data):
    st.subheader('Ingresar registro')
    if st.button('Guardar'):
        data = {
            'peso_sem3' : predicction_data['feature_3'],
            'peso_sem4' : predicction_data['feature_1'],
            'agua' : predicction_data['feature_2'],
            'consumo_acabado' : predicction_data['feature_4'],
            'mortalidad_std' : predicction_data['feature_5'],
            'created_at' : predicction_data['created_at']
        }

        response = client.table('datos_predicciones').insert(data).execute()
        st.success('Registro Creado con Exito')
    return response

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