from modelo import subir_archivo,seleccion_variables,modelo_ensemble,menu_opciones,prediccion
from CRUD_supabase import crear_prediccion
import streamlit as st
from estilos import aplicar_estilos

aplicar_estilos()
#Titulo para el app
st.title("Proyecto Productivo para la prediccion del peso de pollos usando variables descritas por el modelo SelectcKbest luego hacer las predicciones usando el Modelo Ensemble, con Streamlit(v2)")

# Cargar archivo
df = subir_archivo()

if df is not None:
    # Seleccionar las mejores variables
    top5 = seleccion_variables(df)
    if top5:
        # Entrenar el modelo ensemble
        modelo, y_pred_model, y_test_model, x_train_model, y_train_model = modelo_ensemble(top5, df)

        # Menú de opciones para interactuar con el modelo
        input_data, datos = menu_opciones(modelo, y_pred_model, y_test_model, df, x_train_model, y_train_model)

        # Botón para realizar predicción
        if st.button('Realizar Predicción'):
            datos_edit = prediccion(modelo, input_data, datos)

            # Mostrar datos predichos antes de guardar
            st.write("### Resultado de la predicción:")
            st.write(datos_edit)

            # Botón para guardar los datos en Supabase
            if st.button('Guardar'):
                try:
                    crear_prediccion(datos_edit)
                    st.success('Datos guardados correctamente en Supabase.')
                except Exception as e:
                    st.error(f"Error al guardar los datos: {e}")

else:
    st.write("No se ha cargado ningún archivo.")

'''
df = subir_archivo()

if df is not None:
    top5 = seleccion_variables(df)
    if top5:
        modelo,y_pred_model,y_test_model,x_train_model,y_train_model = modelo_ensemble(top5,df)
        input_data,datos = menu_opciones(modelo,y_pred_model,y_test_model,df,x_train_model,y_train_model)
        if st.button('Realizar Prediccion'):
            datos_edit = prediccion(modelo,input_data,datos)
            if st.button('Guardar'):
                crear_prediccion(datos_edit)
                st.success('Datos guardados correctamente')

else:
    st.write("No se ha cargado ningún archivo.")


'''
