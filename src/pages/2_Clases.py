import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    r"C:\Users\andyv\OneDrive\Desktop\andy\trabajo Andy\EVOLVE\Data science\python\proyecto\data\processed\clean_airline_passenger_satisfaction.csv"
)

st.title("🛫 Satisfacción por clase")

fig, ax = plt.subplots(figsize=(10, 8))

sns.countplot(data=df, x="class", hue="satisfaction", ax=ax)

for p in ax.patches:
    height = int(p.get_height())
    ax.annotate(
        str(height),
        (p.get_x() + p.get_width() / 2, height),
        ha='center',
        va='bottom'
    )

st.pyplot(fig)