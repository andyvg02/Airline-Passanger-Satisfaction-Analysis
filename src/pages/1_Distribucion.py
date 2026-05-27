import streamlit as st
import plotly.express as px
from utils import load_data

# Manejo seguro del session_state
if "df_filtered" not in st.session_state:
    st.warning("No se han aplicado filtros aún. Usando datos completos.")
    df = load_data()
else:
    df = st.session_state["df_filtered"]

st.title("📊 Distribución de satisfacción")

# Gráfico interactivo
fig = px.histogram(
    df,
    x="satisfaction",
    color="satisfaction",
    text_auto=True,
    title="Distribución de satisfacción",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_layout(
    bargap=0.2,
    plot_bgcolor="white",
    title_x=0.3
)

st.plotly_chart(fig, use_container_width=True)

# Histograma de edades
st.subheader("Distribución de edades")

fig_age = px.histogram(
    df,
    x="age",
    nbins=30,
    title="Distribución de edades",
    color_discrete_sequence=["#1E88E5"]
)

st.plotly_chart(fig_age, use_container_width=True)