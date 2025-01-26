from modelo import subir_archivo, seleccion_variables, modelo_ensemble, menu_opciones, prediccion
from CRUD_supabase import crear_prediccion, listar_registros, verificar_registros, eliminar_prediccion_rpc
import streamlit as st
from estilos import aplicar_estilos

aplicar_estilos()

# Dividir la pantalla en dos secciones (30% izquierda, 70% derecha)
col1, col2 = st.columns([3, 7])

# Sección de integrantes del grupo (30% - izquierda)
with col1:
    st.title("Integrantes del Grupo")
    st.write("Aquí puedes listar los integrantes del grupo.")
     # Integrante 1
     # URL de la imagen (asegúrate de que sea válida)
    url_imagen_1 = "https://i.imgur.com/ZX7HTol.jpeg"  # Ejemplo de imagen pública

    # Mostrar la imagen
    '''st.markdown('<div class="integrante">', unsafe_allow_html=True)
    st.image(url_imagen_1, caption="Integrante Numero 1", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)'''

    st.write("- Integrante 1")
    st.write("- Integrante 2")
    st.write("- Integrante 3")

# Sección principal (70%)
with col2:
    
    # Título para el app
    st.title("Proyecto Productivo para la predicción del peso de pollos usando variables descritas por el modelo SelectKBest, luego hacer las predicciones usando el Modelo Ensemble, con Streamlit(v2)")

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

            # Mostrar botones solo si la opción seleccionada es "Predicción"
            if st.session_state.get('opcion_seleccionada') == "Predicción":
                # Botón para realizar predicción
                if st.button('Realizar Predicción'):
                    # Generar predicción y guardar en el estado de sesión
                    st.session_state['datos_edit'] = prediccion(modelo, input_data, datos)

                # Verificar si hay datos disponibles para guardar
                if st.session_state['datos_edit'] is not None:
                    # Botón para guardar los datos en Supabase
                    if st.button('Guardar'):
                        crear_prediccion(st.session_state['datos_edit'])
                        st.success('Datos guardados correctamente en Supabase.')
                        # Limpiar el estado después de guardar
                        st.session_state['datos_edit'] = None

                # Botones para listar y eliminar registros
                if verificar_registros():
                    if st.button('Listar Registros'):
                        listar_registros()
                    
                    # Campo para ingresar el ID a eliminar
                    prediccion_id =int( st.number_input("Ingresa el ID del registro que deseas eliminar:", min_value=1))
                    
                    # Botón para confirmar la eliminación
                    if st.button('Eliminar Registro'):
                        if eliminar_prediccion_rpc(prediccion_id):
                            # Actualizar la lista de registros después de eliminar
                            st.rerun()

    else:
        st.write("No se ha cargado ningún archivo.")

