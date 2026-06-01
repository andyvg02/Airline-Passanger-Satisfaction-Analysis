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

# Eliminar ID si existe
id_cols = [c for c in df_model.columns if "id" in c.lower() or "unnamed" in c.lower()]
df_model = df_model.drop(columns=id_cols)

# ---------------------------------------------------------
# Separar categóricas y numéricas
# ---------------------------------------------------------
cat_cols = df_model.select_dtypes(exclude="number").columns.tolist()
cat_cols.remove("satisfaction")

# Mantener age_group y eliminar age si existe
if "age" in df_model.columns:
    df_model = df_model.drop(columns=["age"])
if "age" in cat_cols:
    cat_cols.remove("age")

num_cols = df_model.select_dtypes(include="number").columns.tolist()
num_cols.remove("target")

# Quitar total_delay porque se calcula automáticamente
if "total_delay" in num_cols:
    num_cols.remove("total_delay")

# ---------------------------------------------------------
# One-hot encoding para el modelo
# ---------------------------------------------------------
df_encoded = pd.get_dummies(df_model[cat_cols + num_cols], drop_first=True)
X = df_encoded
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

with st.form("form_prediccion"):
    cols = st.columns(3)

    # -------------------------
    # CATEGÓRICAS (incluye age_group)
    # -------------------------
    for i, col in enumerate(cat_cols):
        with cols[i % 3]:
            options = sorted(df[col].dropna().unique())
            inputs[col] = st.selectbox(
                col.replace("_", " ").capitalize(),
                options=options
            )

    # -------------------------
    # NUMÉRICAS (excepto total_delay)
    # -------------------------
    for i, col in enumerate(num_cols):
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        mean_val = float(df[col].mean())

        with cols[i % 3]:
            inputs[col] = st.slider(
                col.replace("_", " ").capitalize(),
                min_value=min_val,
                max_value=max_val,
                value=mean_val
            )

    # -------------------------
    # Cálculo automático del total_delay
    # -------------------------
    if "departure_delay" in inputs and "arrival_delay" in inputs:
        inputs["total_delay"] = inputs["departure_delay"] + inputs["arrival_delay"]

    submitted = st.form_submit_button("🔍 Predecir satisfacción")

# ---------------------------------------------------------
# Predicción
# ---------------------------------------------------------
if submitted:
    input_df = pd.DataFrame([inputs])

    # One-hot encoding igual que el entrenamiento
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=X.columns, fill_value=0)

    # Escalar
    input_scaled = scaler.transform(input_encoded)

    # Predicción
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