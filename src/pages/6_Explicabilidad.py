import streamlit as st
import pandas as pd
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
Si SHAP está instalado, verás explicaciones del modelo.
Si no está instalado, la página seguirá funcionando sin errores.
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
# Intentar cargar SHAP
# ---------------------------------------------------------
try:
    import shap

    st.success("SHAP cargado correctamente.")

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_scaled)

    st.subheader("🌍 Importancia global (SHAP)")
    shap.summary_plot(shap_values[1], X, show=False)
    st.pyplot(bbox_inches="tight")

except Exception as e:
    st.error("⚠️ SHAP no está instalado o falló al cargar.")
    st.info("Instala SHAP con:  pip install shap  o  conda install -c conda-forge shap")
    st.text(str(e))
