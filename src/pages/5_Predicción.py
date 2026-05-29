import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from utils import load_data

# ---------------------------------------------------------
# Cargar datos filtrados o completos
# ---------------------------------------------------------
if "df_filtered" not in st.session_state:
    st.warning("No se han aplicado filtros aún. Usando datos completos.")
    df = load_data()
else:
    df = st.session_state["df_filtered"]

st.title("🔮 Predicción interactiva de satisfacción")

st.markdown("""
Introduce las características del pasajero y el modelo predecirá si estará **satisfecho** o **insatisfecho**.
""")

# ---------------------------------------------------------
# Preparar datos para entrenar el modelo
# ---------------------------------------------------------
df_model = df.copy()
df_model["target"] = (df_model["satisfaction"] == "satisfied").astype(int)

X = df_model.select_dtypes(include="number").drop(columns=["target"])
y = df_model["target"]

# Entrenar modelo
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_scaled, y)

# ---------------------------------------------------------
# Formulario interactivo
# ---------------------------------------------------------
st.subheader("📝 Introduce los valores del pasajero")

inputs = {}

for col in X.columns:
    min_val = float(df[col].min())
    max_val = float(df[col].max())
    mean_val = float(df[col].mean())

    inputs[col] = st.slider(
        col.replace("_", " ").capitalize(),
        min_value=min_val,
        max_value=max_val,
        value=mean_val
    )

# Convertir a dataframe
input_df = pd.DataFrame([inputs])

# Escalar igual que el entrenamiento
input_scaled = scaler.transform(input_df)

# ---------------------------------------------------------
# Predicción
# ---------------------------------------------------------
if st.button("🔍 Predecir satisfacción"):
    proba = model.predict_proba(input_scaled)[0][1]
    pred = model.predict(input_scaled)[0]

    st.markdown("---")

    if pred == 1:
        st.success("✅ **El modelo predice que el pasajero estará SATISFECHO.**")
    else:
        st.error("❌ **El modelo predice que el pasajero estará INSATISFECHO.**")

    st.metric("Probabilidad de satisfacción", f"{proba*100:.2f}%")

    st.markdown("---")
    st.info("Esta predicción se basa en el modelo Random Forest entrenado con los datos filtrados.")
