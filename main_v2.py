from modelo import subir_archivo,seleccion_variables,modelo_ensemble,menu_opciones,aplicar_estilos
from CRUD_supabase import crear_prediccion,read_prediccion,update_prediccion,delete_prediccion,listar_registros,main_menu
import streamlit as st

aplicar_estilos()
#Titulo para el app
st.title("Proyecto Productivo para la prediccion del peso de pollos usando variables descritas por el modelo SelectcKbest luego hacer las predicciones usando el Modelo Ensemble, con Streamlit(v2)")

df = subir_archivo()
top5 = seleccion_variables(df)
modelo,y_pred_model,y_test_model,x_train_model,y_train_model = modelo_ensemble(top5,df)
menu_opciones(modelo,y_pred_model,y_test_model,df,x_train_model,y_train_model)


