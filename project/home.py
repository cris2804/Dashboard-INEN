import streamlit as st
import pandas as pd
import plotly.express as px
from   streamlit_option_menu import option_menu
import time
import os
import numpy as np
# from numerize.numerize import numerize
# set page config para la configuracion de la pagina
st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide",
    # initial_sidebar_state="expanded",
)

page_bg = """
<style>
    [data-testid="stAppViewContainer"]{
    background-color: #FFFFFF;
    color:black;
    }
    [data-testid="stHeader"]{
    background-color: #224E90;
    color:black;
    height: 70px;
    
    }
    [data-testid="stSidebarContent"]{
    background: #063D81;
    }
    [data-testid="stAppViewBlockContainer"]{
        background-color: #224E90;
        padding:4rem 1rem 2rem;

    }
    [data-testid="stHorizontalBlock"]{
        
        color:white;
        
        
    }
   
    div[data-baseweb="select"] > div {
    background-color: #B5904F;
}


   
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)
image_path = "logoINEN.png"


# Contenedor con fondo estilizado
headerr = st.container()
with headerr:
    col1, col2, col3 = st.columns([0.5, 4, 2],vertical_alignment="bottom")
    
    with col1:
        # ima,_ = st.columns([1,0])
        # with ima:
        st.image(image_path, width=120)
    
    with col2:
# Centrar y estilizar el texto dentro de la columna
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;font-size: 120px;">
                <h2 style="color: white; text-align: center;">Análisis Integral de Ingresos Hospitalarios y Egresos en Perú</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )    
    with col3:
        left, middle, right = st.columns(3, vertical_alignment="bottom")
        left.selectbox("MES", ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"])
        middle.selectbox("MACROREGION", ["NORTE", "SUR", "CENTRO", "ORIENTE", "LIMA METROPOLITANA"])
        right.selectbox(
        "DEPARTAMENTO", [
        "AMAZONAS",
        "ANCASH",
        "APURIMAC",
        "AREQUIPA",
        "AYACUCHO",
        "CAJAMARCA",
        "CALLAO",
        "CUSCO",
        "HUANCAVELICA",
        "HUANUCO",
        "ICA",
        "JUNIN",
        "LA LIBERTAD",
        "LAMBAYEQUE",
        "LIMA",
        "LORETO",
        "MADRE DE DIOS",
        "MOQUEGUA",
        "PASCO",
        "PIURA",
        "PUNO",
        "SAN MARTIN",
        "TACNA",
        "TUMBES",
        "UCAYALI"
    ])
        # st.selectbox("MES", ["Enero", "Febrero", "Marzo"])
        # st.selectbox("MACROREGION", ["Norte", "Sur", "Centro", "Oriente"])
        # st.selectbox("DEPARTAMENTO", ["Lima", "Cusco", "Piura", "Arequipa"])
  
# Definir el estilo para contenedores
container_style = lambda height: f"""
    <div style="background-color: white;box-shadow: 0px 4px 8px 2px rgba(0, 0, 0, 0.25);
; height: {height}px; padding: 10px; border-radius: 20px;margin-bottom: 9px">
 .
    </div>
"""
container_style_2 = lambda height: f"""
    <div style="
        box-shadow: inset 0px 4px 8px 2px rgba(0, 0, 0, 0.25), 0px 4px 8px 2px rgba(0, 0, 0, 0.25);
        height: {height}px; 
        padding: 10px;
        margin-bottom: 9px;
        border-radius: 20px;
        background: #D5EBFF;
    ">
    .
    </div>
"""
contiene1, contiene2, contiene3 = st.columns([1, 0.8, 1],vertical_alignment="bottom")
# Contenedores en la primera columna
with contiene1:
    st.markdown(container_style_2(100), unsafe_allow_html=True)  # Contenedor de 50px
    st.markdown(container_style(400), unsafe_allow_html=True)  # Contenedor que ocupa el resto (altura ajustable)

# Contenedores en la segunda columna
with contiene2:
    st.markdown(container_style(200), unsafe_allow_html=True)  # Primer contenedor (altura ajustable)
    st.markdown(container_style(300), unsafe_allow_html=True)  # Segundo contenedor (altura ajustable)

# Contenedores en la tercera columna
with contiene3:
    st.markdown(container_style(250), unsafe_allow_html=True)  # Primer contenedor (altura ajustable)
    st.markdown(container_style(250), unsafe_allow_html=True)  # Segundo


#############################
# Estilo personalizado para la barra de progreso
st.markdown(
    """
    <style>
    .progress-bar-container {
        width: 100%;
        background-color: #f3f3f3;
        border-radius: 25px;
        padding: 3px;
        margin: 10px 0;
    }

    .progress-bar {
        background-color: #4CAF50;
        width: 0%;
        height: 30px;  /* Cambia este valor para ajustar el grosor */
        border-radius: 25px;
        text-align: center;
        color: white;
        line-height: 30px;  /* Asegura que el texto esté centrado verticalmente */
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True
)

# Crear el contenedor de la barra de progreso
progress_placeholder = st.empty()

for percent_complete in range(101):
    progress_text = f"{percent_complete}% completed"
    progress_bar_html = f"""
    <div class="progress-bar-container">
        <div class="progress-bar" style="width: {percent_complete}%;">{progress_text}</div>
    </div>
    """
    progress_placeholder.markdown(progress_bar_html, unsafe_allow_html=True)
    time.sleep(0.05)  # Simula el progreso con un retraso

st.button("Rerun")







###################
st.sidebar.header("Home qq")
