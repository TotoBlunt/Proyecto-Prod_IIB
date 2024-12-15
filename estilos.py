#Interfaz de Strreamlit

def aplicar_estilos():
    st.markdown(
        """
        <style>
        .stButton button {
            background-color: #4CAF50 !important; /* Color de fondo del botón */
            color: white !important; /* Color del texto del botón */
        }
        .stTextInput input {
            background-color: #f0f0f0 !important; /* Color de fondo del input */
            color: #333333 !important; /* Color del texto del input */
        }
        .stTextArea textarea {
            background-color: #f0f0f0 !important; /* Color de fondo del textarea */
            color: #000000 !important; /* Color del texto del textarea */
        }
        .stSelectbox select {
            background-color: #f0f0f0 !important; /* Color de fondo del select */
            color: #333333 !important; /* Color del texto del select */
        }
        .stMarkdown {
            color: #FFFFFF !important; /* Color del texto en markdown */
        }
        .stSuccess {
            color: #4CAF50 !important; /* Color del texto en mensajes de éxito */
        }
        .stError {
            color: #FF5252 !important; /* Color del texto en mensajes de error */
        }
        .stApp {
            background-color:  #CCDDDD !important; /* Color de fondo de la aplicación */
        }
        </style>
        """,
        unsafe_allow_html=True)