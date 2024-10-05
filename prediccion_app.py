import streamlit as st
import pickle
import numpy as np

# Cargar el modelo solo si se ha establecido el estado
if 'go_to_prediction' in st.session_state and st.session_state.go_to_prediction:
    # Título de la aplicación de predicción
    st.title("Predicción con VotingRegressor")

    # Cargar el modelo
    with open('voting_regressor_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Entradas de datos para las características
    feature_1 = st.number_input('Ingresa el valor para Feature 1')
    feature_2 = st.number_input('Ingresa el valor para Feature 2')
    feature_3 = st.number_input('Ingresa el valor para Feature 3')
    feature_4 = st.number_input('Ingresa el valor para Feature 4')
    feature_5 = st.number_input('Ingresa el valor para Feature 5')

    # Botón para realizar la predicción
    if st.button('Realizar Predicción'):
        # Validar que las entradas no estén vacías
        if feature_1 is not None and feature_2 is not None and feature_3 is not None and feature_4 is not None and feature_5 is not None:
            # Crear el array con los datos de entrada
            input_data = np.array([[feature_1, feature_2, feature_3,feature_4,feature_5]])

            # Hacer la predicción con el modelo
            prediction = model.predict(input_data)

            # Mostrar el resultado de la predicción
            st.write(f'La predicción del modelo es: {prediction[0]:.2f}')  # Formato de dos decimales
        else:
            st.error("Por favor, ingresa valores válidos para todas las características.")


    # Botón para volver a la aplicación principal
    if st.button('Volver a la Aplicación Principal'):
        st.session_state.go_to_prediction = False
        st.experimental_rerun()  # Recargar la aplicación para volver al estado anterior