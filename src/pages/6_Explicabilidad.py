import streamlit as st
import pandas as pd
import shap
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

st.title("🧠 Explicabilidad del modelo (SHAP)")

st.markdown("""
Esta página muestra **cómo y por qué** el modelo Random Forest toma decisiones.
SHAP permite entender la contribución de cada variable en la predicción.
""")

# ---------------------------------------------------------
# Preparar datos
# ---------------------------------------------------------
df_model = df.copy()
df_model["target"] = (df_model["satisfaction"] == "satisfied").astype(int)

X = df_model.select_dtypes(include="number").drop(columns=["target"])
y = df_model["target"]

# Escalado
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenar modelo
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_scaled, y)

# ---------------------------------------------------------
# SHAP
# ---------------------------------------------------------
st.subheader("📌 Cálculo de valores SHAP")

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_scaled)

st.success("Valores SHAP calculados correctamente.")

# ---------------------------------------------------------
# Importancia global (beeswarm)
# ---------------------------------------------------------
st.subheader("🌍 Importancia global de variables")

st.markdown("Este gráfico muestra qué variables influyen más en el modelo.")

fig_bee = shap.plots.beeswarm(shap_values[1], max_display=15, show=False)
st.pyplot(bbox_inches="tight")

# ---------------------------------------------------------
# Importancia media
# ---------------------------------------------------------
st.subheader("📊 Importancia media (SHAP)")

shap.summary_plot(shap_values[1], X, plot_type="bar", show=False)
st.pyplot(bbox_inches="tight")

# ---------------------------------------------------------
# Explicación individual
# ---------------------------------------------------------
st.subheader("🔍 Explicación de una predicción individual")

index = st.slider("Selecciona un pasajero del dataset", 0, len(X)-1, 0)

st.write("Características del pasajero seleccionado:")
st.dataframe(pd.DataFrame([X.iloc[index]], index=["Valores"]))

st.markdown("### Waterfall de la predicción")

shap_value_single = explainer.shap_values(X_scaled[index:index+1])

shap.plots.waterfall(shap_value_single[1][0], show=False)
st.pyplot(bbox_inches="tight")