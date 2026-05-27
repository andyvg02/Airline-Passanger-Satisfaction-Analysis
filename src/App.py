import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Airline Satisfaction Dashboard",
    layout="wide"
)

df = pd.read_csv(
    r"C:\Users\andyv\OneDrive\Desktop\andy\trabajo Andy\EVOLVE\Data science\python\proyecto\data\processed\clean_airline_passenger_satisfaction.csv"
)

st.title("✈️ Airline Passenger Satisfaction Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Número pasajeros", len(df))
col2.metric("Retraso medio", round(df["total_delay"].mean(), 2))
col3.metric("Edad media", round(df["age"].mean(), 1))

st.write("Selecciona una página en el menú lateral para ver los análisis.")