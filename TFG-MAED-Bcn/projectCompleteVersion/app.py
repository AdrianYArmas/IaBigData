import streamlit as st
import requests
import pandas as pd
from streamlit_extras.stylable_container import stylable_container

# Estilos personalizados
st.markdown("""
    <style>
    h1 {
        font-size: 2rem !important;
        margin-top: -2rem !important;
        margin-bottom: 1rem !important;
    }

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

    div[class="stDateInput"] input {
        color: white !important;
        background-color: #333333 !important;
        border-radius: 5px !important;
        padding: 0.5em;
    }

    .st-f0::after { background-color: #007BFF; }
    .st-eu::after { border-left-color: #007BFF; }
    .st-es::after { border-bottom-color: #007BFF; }
    .st-er::after { border-top-color: #007BFF; }
    .st-et::after { border-right-color: #007BFF; }

    .st-b3, .st-b4, .st-b5, .st-b6, .st-by, .st-bx, .st-bz, .st-c0 {
        border-color: white;
    }

    /* Estilo común para los cuadros de resultados */
    .result-box {
        padding: 1.2em;
        border-radius: 10px;
        color: black;
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 1em;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        text-align: center;

        /* Dimensiones iguales */
        width: 100%;
        min-height: 180px;

        /* Centramos el contenido vertical y horizontalmente */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)


def cuadro_resultado(titulo, contenido, color_hex, emoji=""):
    return f"""
    <div class="result-box" style="background-color:{color_hex};">
        <strong>{emoji} {titulo}</strong><br>
        {contenido}
    </div>
    """


st.title("Predicción de Consumo por Intervalo de Fechas")

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

                max_dia = df['prediccion'].idxmax().date()
                max_valor_kwh = df['prediccion'].max()
                max_valor_gwh = max_valor_kwh / 1_000_000

                min_dia = df['prediccion'].idxmin().date()
                min_valor_kwh = df['prediccion'].min()
                min_valor_gwh = min_valor_kwh / 1_000_000

                # Mostrar resultados en columnas
                col_tot, col_med, col_max, col_min = st.columns(4)

                with col_tot:
                    st.markdown(
                        cuadro_resultado(
                            "Consumo total estimado",
                            f"{total_consumo_kwh:,.2f} kWh<br>({total_consumo_gwh:,.2f} GWh)",
                            "#90ee90", 
                            "📊"
                        ),
                        unsafe_allow_html=True
                    )
                with col_med:
                    st.markdown(
                        cuadro_resultado(
                            "Consumo medio diario",
                            f"{media_consumo_kwh:,.2f} kWh<br>({media_consumo_gwh:,.4f} GWh)",
                            "#87cefa",  
                            "📊"
                        ),
                        unsafe_allow_html=True
                    )
                with col_max:
                    st.markdown(
                        cuadro_resultado(
                            "Máxima demanda estimada",
                            f"{max_valor_kwh:,.2f} kWh<br>({max_valor_gwh:,.4f} GWh)<br>📅 Día: <strong>{max_dia}</strong>",
                            "#FFA500",  
                            "📈"
                        ),
                        unsafe_allow_html=True
                    )
                with col_min:
                    st.markdown(
                        cuadro_resultado(
                            "Mínima demanda estimada",
                            f"{min_valor_kwh:,.2f} kWh<br>({min_valor_gwh:,.4f} GWh)<br>📅 Día: <strong>{min_dia}</strong>",
                            "#FFFF99",  
                            "📉"
                        ),
                        unsafe_allow_html=True
                    )
        else:
            st.error(f"Error al obtener datos del servidor: {response.status_code}")
