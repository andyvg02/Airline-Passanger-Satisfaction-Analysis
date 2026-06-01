import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


# ============================================================
# 1. Distribución general de satisfacción
# ============================================================
def plot_satisfaction_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="satisfaction", palette="viridis")
    plt.title("Distribución de satisfacción")
    plt.xlabel("Satisfacción")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()


# ============================================================
# 2. Satisfacción por clase
# ============================================================
def plot_satisfaction_by_class(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(
        data=df,
        x="class",
        hue="satisfaction",
        palette="viridis"
    )
    plt.title("Satisfacción por clase")
    plt.xlabel("Clase del vuelo")
    plt.ylabel("Cantidad")
    plt.legend(title="Satisfacción")
    plt.tight_layout()
    plt.show()


# ============================================================
# 3. Satisfacción por tipo de cliente
# ============================================================
def plot_satisfaction_by_customer_type(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(
        data=df,
        x="customer_type",
        hue="satisfaction",
        palette="viridis"
    )
    plt.title("Satisfacción por tipo de cliente")
    plt.xlabel("Tipo de cliente")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()


# ============================================================
# 4. Retraso total vs satisfacción
# ============================================================
def plot_delay_by_satisfaction(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(
        data=df,
        x="satisfaction",
        y="total_delay",
        palette="viridis"
    )
    plt.title("Retraso total según satisfacción")
    plt.xlabel("Satisfacción")
    plt.ylabel("Retraso total (minutos)")
    plt.tight_layout()
    plt.show()


# ============================================================
# 5. Valoración de servicios por satisfacción
# ============================================================
def plot_service_scores_by_satisfaction(df):
    service_cols = [
        "seat_comfort", "inflight_entertainment", "cleanliness",
        "food_and_drink", "onboard_service", "baggage_handling",
        "checkin_service", "wifi_service"
    ]

    mean_scores = df.groupby("satisfaction")[service_cols].mean().T

    plt.figure(figsize=(10, 6))
    mean_scores.plot(kind="bar", figsize=(12, 6), colormap="viridis")
    plt.title("Valoración media de servicios por satisfacción")
    plt.ylabel("Puntuación media")
    plt.xlabel("Servicio")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ============================================================
# 6. Matriz de correlación
# ============================================================
def plot_correlation_matrix(df):
    numeric_df = df.select_dtypes(include="number")
    corr = numeric_df.corr()

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, cmap="coolwarm", annot=False)
    plt.title("Matriz de correlación")
    plt.tight_layout()
    plt.show()


# ============================================================
# 7. Satisfacción por grupo de edad
# ============================================================
def plot_satisfaction_by_age_group(df):
    if "age_group" not in df.columns:
        print("⚠️ La columna 'age_group' no existe. Debes crearla en features.py")
        return

    plt.figure(figsize=(8, 5))
    sns.countplot(
        data=df,
        x="age_group",
        hue="satisfaction",
        palette="viridis"
    )
    plt.title("Satisfacción por grupo de edad")
    plt.xlabel("Grupo de edad")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()