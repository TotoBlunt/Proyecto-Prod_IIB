# Proyecto-IDL3
* Ruta Streamlit v1: https://proyecto-appiib-hmtgjbf8v6cgjg33agakib.streamlit.app/
* Ruta Streamlit v2: https://proyecto-v2.streamlit.app/
# Proyecto de Predicción del Peso de Pollos

Este proyecto tiene como objetivo predecir el peso final de los pollos basándose en un conjunto de variables seleccionadas mediante el modelo `SelectKBest`. Para realizar las predicciones, se utiliza un modelo de ensamble que combina varios algoritmos de aprendizaje automático, tales como : Regresion Lineal, Arbol de Decision, Bosques de Decision,Vecinos Cercanos y GradientBoosting. La interfaz de usuario se ha desarrollado utilizando Streamlit, lo que permite una interacción sencilla y eficiente con el modelo.

## Características principales

- **Selección de variables**: Utiliza el modelo `SelectKBest` para seleccionar las 5 variables más relevantes para la predicción del peso de los pollos.
- **Modelo de ensamble**: Combina múltiples modelos de aprendizaje automático para mejorar la precisión de las predicciones.
- **Interfaz de usuario**: Desarrollada con Streamlit, permite cargar datos, realizar predicciones y visualizar resultados de manera intuitiva.
- **Integración con Supabase**: Los resultados de las predicciones pueden guardarse en una base de datos Supabase para su posterior consulta y análisis.

## Estructura del proyecto

El proyecto está organizado en varios archivos Python que se han unido en un archivo principal (`main.py`). A continuación se describe la función de cada archivo:

- **main.py**: Archivo principal que ejecuta la aplicación Streamlit y gestiona la interacción del usuario.
- **modelo.py**: Contiene las funciones para cargar datos, seleccionar variables, entrenar el modelo de ensamble y realizar predicciones.
- **CRUD_supabase.py**: Gestiona las operaciones CRUD (Crear, Leer, Eliminar) con la base de datos Supabase.
- **estilos.py**: Define los estilos CSS aplicados a la interfaz de usuario de Streamlit.
- **supabase_connector.py**: Gestiona la conexion y las clases del supabase.

## Requisitos previos

Para ejecutar este proyecto, necesitas tener instalado Python 3.7 o superior. Además, debes instalar las siguientes bibliotecas con **pip install 'Biblioteca'**:

pandas
openpyxl
scikit-learn
matplotlib
streamlit
numpy
supabase==0.5.3
datetime
requests

## Clonar Repositorio

Desde el cmd:

git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

## Ejecutar la Aplicacion

Desde el cmd:
streamlit run main.py

## Uso de la Aplicacion

1. Cargar datos: Sube un archivo CSV con los datos de los pollos.

2. Seleccionar variables: El modelo SelectKBest seleccionará automáticamente las 5 variables más relevantes.

3. Realizar predicciones: Utiliza el modelo de ensamble para predecir el peso de los pollos.

4. Guardar resultados: Los resultados de las predicciones pueden guardarse en Supabase para su posterior consulta.

5. Grafico de comparación en la predicción: Este gráfico muestra el peso final real vs el peso final predicho para su posterior análisis.

6. Metricas de Evaluación del Modelo: Este apartado nos muestra las metricas de evaluación mas importantes del modelo tales como el error cuadratico medio(MSE),error absoluto medio(MAE), coeficiente de determinacion (r2), y el promedio de r2 en validacion cruzada.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.

2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

3. Realiza tus cambios y haz commit (git commit -am 'Añade nueva funcionalidad').

4. Haz push a la rama (git push origin feature/nueva-funcionalidad).

5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de mi perfil de GitHub.
