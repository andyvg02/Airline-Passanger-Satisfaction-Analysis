import streamlit as st
import plotly.express as px
from utils import load_data

# Manejo seguro del session_state
if "df_filtered" not in st.session_state:
    st.warning("No se han aplicado filtros aún. Usando datos completos.")
    df = load_data()
else:
    df = st.session_state["df_filtered"]

st.title("🛫 Satisfacción por clase")

fig = px.histogram(
    df,
    x="class",
    color="satisfaction",
    barmode="group",
    text_auto=True,
    title="Satisfacción por clase",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_layout(
    plot_bgcolor="white",
    title_x=0.3
)

st.plotly_chart(fig, use_container_width=True)

# Boxplot de retrasos por clase
st.subheader("Retrasos por clase")

fig_box = px.box(
    df,
    x="class",
    y="total_delay",
    color="class",
    title="Distribución de retrasos por clase",
    color_discrete_sequence=px.colors.qualitative.Set2
)

st.plotly_chart(fig_box, use_container_width=True)