from modelo import subir_archivo,seleccion_variables,modelo_ensemble,menu_opciones,prediccion
from CRUD_supabase import crear_prediccion,listar_registros,verificar_registros
import streamlit as st
from estilos import aplicar_estilos

aplicar_estilos()

#Titulo para el app
st.title("Proyecto Productivo para la prediccion del peso de pollos usando variables descritas por el modelo SelectcKbest luego hacer las predicciones usando el Modelo Ensemble, con Streamlit(v2)")

# Estado de sesión para manejar datos entre interacciones
if 'datos_edit' not in st.session_state:
    st.session_state['datos_edit'] = None

# Cargar archivo
df = subir_archivo()

if df is not None:
    # Selección de las mejores variables
    top5 = seleccion_variables(df)
    if top5:
        # Entrenamiento del modelo ensemble
        modelo, y_pred_model, y_test_model, x_train_model, y_train_model = modelo_ensemble(top5, df)

        # Menú de opciones (Predicción, Métricas, Gráfico, etc.)
        input_data, datos = menu_opciones(modelo, y_pred_model, y_test_model, df, x_train_model, y_train_model)

        # Botón para realizar predicción
        if st.button('Realizar Predicción'):
            # Generar predicción y guardar en el estado de sesión
            st.session_state['datos_edit'] = prediccion(modelo, input_data, datos)

            # Mostrar los datos predichos
            #st.write("### Resultado de la predicción:")
            #st.write(st.session_state['datos_edit'])
        if verificar_registros():
            if st.button('Listar Registro'):
                listar_registros()
            if st.button('Elminar Registro'):
                listar_registros()
                # Campo para ingresar el ID a eliminar
                prediccion_id = st.number_input("Ingresa el ID del registro que deseas eliminar:", min_value=1)
                if st.button('Eliminar'):
                    eliminar_prediccion(prediccion_id)
                    # Actualizar la lista de registros después de eliminar
                    st.experimental_rerun()
                   
            
        # Verificar si hay datos disponibles para guardar
        if st.session_state['datos_edit'] is not None:
            # Botón para guardar los datos en Supabase
            if st.button('Guardar'):
                crear_prediccion(st.session_state['datos_edit'])
                st.success('Datos guardados correctamente en Supabase.')
                # Limpiar el estado después de guardar
                st.session_state['datos_edit'] = None
            

                

else:
    st.write("No se ha cargado ningún archivo.")



