import streamlit as st
import numpy as np
from datetime import datetime
from supabase_connector import crear_cliente
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# Crear cliente de Supabase
client = crear_cliente()

def crear_prediccion(predicction_data):
    st.subheader('Ingresar registro')
    
    # Verificar que predicction_data contenga los datos necesarios
    required_keys = ['feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5', 'created_at', 'prediction']
    for key in required_keys:
        if key not in predicction_data[0]:
            st.error(f"Falta la clave '{key}' en predicction_data")
            return
    
    # Crear el diccionario de datos a insertar
    data = {
        'peso_sem3': predicction_data[0]['feature_3'],
        'peso_sem4': predicction_data[0]['feature_1'],
        'agua': predicction_data[0]['feature_2'],
        'consumo_acabado': predicction_data[0]['feature_4'],
        'mortalidad_std': predicction_data[0]['feature_5'],
        'created_at': predicction_data[0]['created_at'],
        'prediction': predicction_data[0]['prediction']
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

# Menú principal
def main_menu():
    st.title("Aplicación de Predicción")
    page = st.selectbox("### Selecciona una opción", ["Predicción", 'Grafico de Comparacion en la Prediccion', 'Metricas de Evaluacion del Modelo'])
    
    if page == 'Metricas de Evaluacion del Modelo':
        # Calcular métricas de evaluación
        st.write('### Metricas de Evaluacion del "Modelo Final(VotingRegresor)":\n')
        mse = mean_squared_error(y_test_model, y_pred_model)
        r2 = r2_score(y_test_model, y_pred_model)
        mae = mean_absolute_error(y_test_model, y_pred_model)
        st.write(f'#### Coeficiente de determinacion(R²): {r2:.4f}')
        st.write(f'#### Error cuadratico medio(MSE): {mse:.4f}')
        st.write(f'#### Error absoluto medio(MAE): {mae:.4f}')
        # Validación Cruzada del modelo Voting
        r2_scores = cross_val_score(modelo, x_train_model, y_train_model, cv=5, scoring='r2')
        st.write(f'#### R² promedio en validación cruzada: {r2_scores.mean():.4f}')
    
    elif page == 'Grafico de Comparacion en la Prediccion':
        st.write('### Grafico de Comparacion en la Prediccion')
        # Gráfico de Comparación
        fig, ax = plt.subplots()
        ax.plot(df['PesoFinal'], label='Peso Prom. Final (Real)', color='blue')
        ax.plot(df['Peso Prom Final Predicho'], label='Peso Prom. Final Predicho', color='red')
        ax.set_xlabel('Índice')
        ax.set_ylabel('Peso Prom. Final')
        ax.set_title('Comparación entre Peso Prom. Final Real y Predicho')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        # Varianza
        varianza = ((df['PesoFinal'] - df['Peso Prom Final Predicho']) ** 2).mean()
        st.write(f"#### La varianza de los valores es: {varianza:.4f}")

    elif page == "Predicción":
        st.title("Aplicación de Predicción")
        # Entradas de datos para las características
        feature_1 = st.number_input('Ingresa el valor para PesoSem4', format="%.3f")
        feature_2 = st.number_input('Ingresa el valor para Agua', format="%.3f")
        feature_3 = st.number_input('Ingresa el valor para PesoSem3', format="%.3f")
        feature_4 = st.number_input('Ingresa el valor para ConsumoAcabado', format="%.3f")
        feature_5 = st.number_input('Ingresa el valor para MortStd', format="%.3f")
        created_at = str(datetime.utcnow())

        # Botón para realizar la predicción
        if st.button('Realizar Predicción'):
            # Validar que las entradas no estén vacías
            if feature_1 is not None and feature_2 is not None and feature_3 is not None and feature_4 is not None and feature_5 is not None:
                # Crear el array con los datos de entrada
                input_data = np.array([[feature_1, feature_2, feature_3, feature_4, feature_5]])

                # Hacer la predicción con el modelo
                prediction = modelo.predict(input_data)
                prediction = round(prediction[0], 2)  # Formato de dos decimales

                # Mostrar el resultado de la predicción
                st.write(f'### La predicción del modelo para Peso Final es : {prediction} kg')
            else:
                st.error("### Por favor, ingresa valores válidos para todas las características.")

            data = {
                'feature_1': feature_1,
                'feature_2': feature_2,
                'feature_3': feature_3,
                'feature_4': feature_4,
                'feature_5': feature_5,
                'created_at': created_at,
                'prediction': prediction
            }
            data_to_insert = [data]
            if st.button('Guardar Datos'):
                crear_prediccion(data_to_insert)
                st.success('Guardado')

if __name__ == "__main__":
    main_menu()