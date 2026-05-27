import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    r"C:\Users\andyv\OneDrive\Desktop\andy\trabajo Andy\EVOLVE\Data science\python\proyecto\data\processed\clean_airline_passenger_satisfaction.csv"
)

st.title("🔥 Mapa de correlaciones")

numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()

fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(corr, cmap="coolwarm", ax=ax)

st.pyplot(fig)