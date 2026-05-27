import streamlit as st
import pandas as pd
from utils import load_data, kpi_color

# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------------
st.set_page_config(
    page_title="Airline Passenger Satisfaction Dashboard",
    layout="wide"
)

# ---------------------------------------------------------
# CARGA DE DATOS
# ---------------------------------------------------------
df = load_data()

st.title("✈️ Airline Passenger Satisfaction Dashboard")

# ---------------------------------------------------------
# FILTROS LATERALES
# ---------------------------------------------------------
st.sidebar.header("Filtros")

# Clase
st.session_state["clases"] = st.sidebar.multiselect(
    "Clase",
    options=sorted(df["class"].unique()),
    default=sorted(df["class"].unique())
)

# Satisfacción
st.session_state["satisf"] = st.sidebar.multiselect(
    "Satisfacción",
    options=sorted(df["satisfaction"].unique()),
    default=sorted(df["satisfaction"].unique())
)

# Edad
age_min, age_max = int(df["age"].min()), int(df["age"].max())
st.session_state["age_range"] = st.sidebar.slider(
    "Rango de edad",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max)
)

# Retraso total
delay_min, delay_max = int(df["total_delay"].min()), int(df["total_delay"].max())
st.session_state["delay_range"] = st.sidebar.slider(
    "Retraso total (min–max)",
    min_value=delay_min,
    max_value=delay_max,
    value=(delay_min, delay_max)
)

# ---------------------------------------------------------
# APLICAR FILTROS
# ---------------------------------------------------------
df_filtered = df[
    (df["class"].isin(st.session_state["clases"])) &
    (df["satisfaction"].isin(st.session_state["satisf"])) &
    (df["age"].between(*st.session_state["age_range"])) &
    (df["total_delay"].between(*st.session_state["delay_range"]))
]

# Guardar para las otras páginas
st.session_state["df_filtered"] = df_filtered

# ---------------------------------------------------------
# KPIs AVANZADOS
# ---------------------------------------------------------
st.markdown("### 📌 Indicadores avanzados")

# Cálculos
satisfaction_rate = (df_filtered["satisfaction"] == "satisfied").mean() * 100
delay_mean = df_filtered["total_delay"].mean()
delay_rate = (df_filtered["total_delay"] > 0).mean() * 100

business_sat = (df_filtered[df_filtered["class"] == "Business"]["satisfaction"] == "satisfied").mean() * 100
eco_sat = (df_filtered[df_filtered["class"] == "Eco"]["satisfaction"] == "satisfied").mean() * 100
eco_plus_sat = (df_filtered[df_filtered["class"] == "Eco Plus"]["satisfaction"] == "satisfied").mean() * 100

# Tarjetas visuales
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    f"{kpi_color(satisfaction_rate, 75, 50)} Satisfacción global",
    f"{satisfaction_rate:.1f}%"
)

col2.metric(
    f"{kpi_color(100 - delay_rate, 80, 60)} Vuelos sin retraso",
    f"{100 - delay_rate:.1f}%"
)

col3.metric(
    f"{kpi_color(100 - delay_mean, 90, 60)} Retraso medio",
    f"{delay_mean:.1f} min"
)

col4.metric(
    "📊 Satisfacción por clase",
    f"B: {business_sat:.0f}% | E+: {eco_plus_sat:.0f}% | E: {eco_sat:.0f}%"
)

st.markdown("---")

# ---------------------------------------------------------
# MENSAJE FINAL
# ---------------------------------------------------------
st.write("Usa el menú lateral para navegar entre las páginas del dashboard.")