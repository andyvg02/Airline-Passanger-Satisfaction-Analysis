import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, roc_curve, auc, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from utils import load_data

# ---------------------------------------------------------
# Cargar datos filtrados
# ---------------------------------------------------------
if "df_filtered" not in st.session_state:
    st.warning("No se han aplicado filtros aún. Usando datos completos.")
    df = load_data()
else:
    df = st.session_state["df_filtered"]

st.title("🤖 Modelos Predictivos de Satisfacción")

st.markdown("""
Esta página entrena modelos predictivos para estimar si un pasajero estará **satisfecho** o **insatisfecho** 
en función de sus características y valoraciones del servicio.
""")

# ---------------------------------------------------------
# Preparación de datos
# ---------------------------------------------------------
df_model = df.copy()

# Convertir target a binario
df_model["target"] = (df_model["satisfaction"] == "satisfied").astype(int)

# Variables numéricas
X = df_model.select_dtypes(include="number").drop(columns=["target"])
y = df_model["target"]

# División train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Escalado
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------------------------------------------------
# Entrenamiento de modelos
# ---------------------------------------------------------
st.subheader("📌 Entrenamiento de modelos")

# Logistic Regression
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train_scaled, y_train)
log_pred = log_reg.predict(X_test_scaled)
log_proba = log_reg.predict_proba(X_test_scaled)[:, 1]

# Random Forest
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_proba = rf.predict_proba(X_test)[:, 1]

st.success("Modelos entrenados correctamente.")

# ---------------------------------------------------------
# Métricas
# ---------------------------------------------------------
st.subheader("📊 Métricas de rendimiento")

col1, col2 = st.columns(2)

col1.metric("Accuracy (Logistic Regression)", f"{log_reg.score(X_test_scaled, y_test):.3f}")
col1.metric("Accuracy (Random Forest)", f"{rf.score(X_test, y_test):.3f}")

col2.metric("F1-score (Logistic Regression)", f"{classification_report(y_test, log_pred, output_dict=True)['weighted avg']['f1-score']:.3f}")
col2.metric("F1-score (Random Forest)", f"{classification_report(y_test, rf_pred, output_dict=True)['weighted avg']['f1-score']:.3f}")

# ---------------------------------------------------------
# Matriz de confusión
# ---------------------------------------------------------
st.subheader("🧩 Matriz de confusión")

cm = confusion_matrix(y_test, rf_pred)

fig_cm = px.imshow(
    cm,
    text_auto=True,
    color_continuous_scale="Blues",
    labels=dict(x="Predicción", y="Real", color="Cantidad"),
    x=["Insatisfecho", "Satisfecho"],
    y=["Insatisfecho", "Satisfecho"],
    title="Matriz de confusión (Random Forest)"
)

st.plotly_chart(fig_cm, use_container_width=True)

# ---------------------------------------------------------
# Curva ROC
# ---------------------------------------------------------
st.subheader("📈 Curva ROC")

fpr, tpr, _ = roc_curve(y_test, rf_proba)
roc_auc = auc(fpr, tpr)

fig_roc = go.Figure()
fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", name="ROC"))
fig_roc.add_trace(go.Scatter(x=[0,1], y=[0,1], mode="lines", name="Azar", line=dict(dash="dash")))

fig_roc.update_layout(
    title=f"Curva ROC (AUC = {roc_auc:.3f})",
    xaxis_title="False Positive Rate",
    yaxis_title="True Positive Rate",
    width=900,
    height=600
)

st.plotly_chart(fig_roc, use_container_width=True)

# ---------------------------------------------------------
# Importancia de variables
# ---------------------------------------------------------
st.subheader("🌟 Importancia de variables (Random Forest)")

importances = pd.DataFrame({
    "feature": X.columns,
    "importance": rf.feature_importances_
}).sort_values("importance", ascending=False)

fig_imp = px.bar(
    importances.head(15),
    x="importance",
    y="feature",
    orientation="h",
    title="Top 15 variables más importantes",
    color="importance",
    color_continuous_scale="Teal"
)

st.plotly_chart(fig_imp, use_container_width=True)