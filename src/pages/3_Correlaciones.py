import streamlit as st
import plotly.express as px
from utils import load_data

# Manejo seguro del session_state
if "df_filtered" not in st.session_state:
    st.warning("No se han aplicado filtros aún. Usando datos completos.")
    df = load_data()
else:
    df = st.session_state["df_filtered"]

st.title("🔥 Mapa de correlaciones (completo, sin números)")

# Seleccionar solo variables numéricas
numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()

# Heatmap completo sin texto
fig = px.imshow(
    corr,
    color_continuous_scale="RdBu_r",
    width=1300,
    height=1200,
    labels=dict(color="Correlación"),
    title="Mapa completo de correlaciones"
)

# Hover limpio con valor exacto
fig.update_traces(
    hovertemplate="Correlación: %{z:.2f}<extra></extra>"
)

# Rotar etiquetas para mejor lectura
fig.update_xaxes(tickangle=45, tickfont=dict(size=14))
fig.update_yaxes(tickfont=dict(size=14))

# Ajustes visuales
fig.update_layout(
    plot_bgcolor="white",
    title_x=0.3,
    margin=dict(l=80, r=80, t=80, b=80)
)

st.plotly_chart(fig, use_container_width=True)