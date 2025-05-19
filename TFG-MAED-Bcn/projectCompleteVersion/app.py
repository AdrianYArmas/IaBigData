import streamlit as st
import requests
import pandas as pd
from streamlit_extras.stylable_container import stylable_container

# Estilos personalizados
st.markdown("""
    <style>
    /* Título más pequeño y con menos margen superior */
    h1 {
        font-size: 2rem !important;
        margin-top: -2rem !important;
        margin-bottom: 1rem !important;
    }
    /* Boton */
    /* Estilo botón mitad ancho y centrado */
    div.stButton > button:first-child,
    div.stButton > button:first-child:focus,
    div.stButton > button:first-child:active {
        background-color: #007BFF;
        color: white !important;
        font-weight: bold;
        border-radius: 5px;
        height: 3em;
        width: 50%;
        display: block;
        margin: auto;
        font-size: 18px;
        border: none;
    }

    div.stButton > button:first-child:hover {
        background-color: #0056b3;
        color: white !important;
    }
    /*Date*/
    /* Input de fecha: texto blanco y borde azul */
    div[class="stDateInput"] input {
        color: white !important;
        background-color: #333333 !important;
        border-radius: 5px !important;
        padding: 0.5em;
    }   

    /**************************************************/
    .st-f0::after {
        background-color: #007BFF;
    }  
    .st-eu::after {
        border-left-color: #007BFF;
    }   
    .st-es::after {
        border-bottom-color: #007BFF;
    }  
    .st-er::after {
        border-top-color: #007BFF;
    }    
    .st-et::after {
        border-right-color: #007BFF;
    }
  
    .st-b3 {
        border-color: white;
    }
     .st-b4 {
        border-color: white;
    }
    .st-b5 {
        border-color: white;
    }
    .st-b6 {
        border-color: white;
    }
    .st-by{
        border-color: white;
    }
    .st-bx{
        border-color: white;
    }
    .st-bz{
        border: white;
    }
    .st-c0{
        border-color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Predicción de Consumo por Intervalo de Fechas")
#streamlit  date selector
# Inputs de fechas
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Fecha inicio")
with col2:
    end_date = st.date_input("Fecha fin")

# Validación de fechas
if start_date > end_date:
    st.error("La fecha de inicio debe ser menor o igual a la fecha de fin.")
else:
    if st.button("Mostrar Predicciones"):
        # Llamada al backend
        url = f"http://127.0.0.1:5000/predict_range?start_date={start_date}&end_date={end_date}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                st.error(f"Error en la predicción: {data['error']}")
            else:
                df = pd.DataFrame(data)
                df['fecha'] = pd.to_datetime(df['fecha'])
                df.set_index('fecha', inplace=True)

                st.line_chart(df['prediccion'])

                # Cálculos
                total_consumo_kwh = df['prediccion'].sum()
                total_consumo_gwh = total_consumo_kwh / 1_000_000

                media_consumo_kwh = df['prediccion'].mean()
                media_consumo_gwh = media_consumo_kwh / 1_000_000

                # Resultados
                st.success(f"Consumo total estimado entre {start_date} y {end_date}: "
                           f"**{total_consumo_kwh:,.2f} kWh** (**{total_consumo_gwh:,.2f} GWh**)")

                st.info(f"Consumo medio diario estimado entre {start_date} y {end_date}: "
                        f"**{media_consumo_kwh:,.2f} kWh** (**{media_consumo_gwh:,.4f} GWh**)")
        else:
            st.error(f"Error al obtener datos del servidor: {response.status_code}")
