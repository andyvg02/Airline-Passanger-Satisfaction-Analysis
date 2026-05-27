import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    r"C:\Users\andyv\OneDrive\Desktop\andy\trabajo Andy\EVOLVE\Data science\python\proyecto\data\processed\clean_airline_passenger_satisfaction.csv"
)

st.title("📊 Distribución de satisfacción")

fig, ax = plt.subplots(figsize=(5, 4))

sns.countplot(data=df, x="satisfaction", ax=ax)

for p in ax.patches:
    count = int(p.get_height())
    ax.annotate(
        str(count),
        (p.get_x() + p.get_width() / 2, count),
        ha='center',
        va='bottom'
    )

st.pyplot(fig)