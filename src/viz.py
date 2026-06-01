from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


# ============================================================
# Helper: guardar figuras
# ============================================================
def save_fig(fig, name: str, folder: Path = Path("figures")) -> None:
    """
    Guarda una figura en la carpeta indicada.
    """
    folder.mkdir(parents=True, exist_ok=True)
    fig.savefig(folder / f"{name}.png", dpi=300, bbox_inches="tight")


# ============================================================
# 1. Distribución general de satisfacción
# ============================================================
def plot_satisfaction_distribution(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="satisfaction",
        hue="satisfaction",     # evita FutureWarning
        palette="viridis",
        legend=False,
        ax=ax
    )

    ax.set_title("Distribución de satisfacción")
    ax.set_xlabel("Satisfacción")
    ax.set_ylabel("Cantidad")

    plt.tight_layout()
    save_fig(fig, "satisfaction_distribution")
    plt.show()


# ============================================================
# 2. Satisfacción por clase
# ============================================================
def plot_satisfaction_by_class(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="class",
        hue="satisfaction",
        palette="viridis",
        ax=ax
    )

    ax.set_title("Satisfacción por clase")
    ax.set_xlabel("Clase del vuelo")
    ax.set_ylabel("Cantidad")
    ax.legend(title="Satisfacción")

    plt.tight_layout()
    save_fig(fig, "satisfaction_by_class")
    plt.show()


# ============================================================
# 3. Satisfacción por tipo de cliente
# ============================================================
def plot_satisfaction_by_customer_type(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="customer_type",
        hue="satisfaction",
        palette="viridis",
        ax=ax
    )

    ax.set_title("Satisfacción por tipo de cliente")
    ax.set_xlabel("Tipo de cliente")
    ax.set_ylabel("Cantidad")

    plt.tight_layout()
    save_fig(fig, "satisfaction_by_customer_type")
    plt.show()


# ============================================================
# 4. Retraso total vs satisfacción
# ============================================================
def plot_delay_by_satisfaction(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="satisfaction",
        y="total_delay",
        hue="satisfaction",     # evita FutureWarning
        palette="viridis",
        legend=False,
        ax=ax
    )

    ax.set_title("Retraso total según satisfacción")
    ax.set_xlabel("Satisfacción")
    ax.set_ylabel("Retraso total (minutos)")

    plt.tight_layout()
    save_fig(fig, "delay_by_satisfaction")
    plt.show()


# ============================================================
# 5. Valoración de servicios por satisfacción
# ============================================================
def plot_service_scores_by_satisfaction(df: pd.DataFrame):
    # Lista completa de columnas esperadas
    expected_cols = [
        "seat_comfort", "inflight_entertainment", "cleanliness",
        "food_and_drink", "on_board_service", "baggage_handling",
        "checkin_service", "inflight_wifi_service"
    ]

    # Filtrar solo las columnas que existen
    service_cols = [col for col in expected_cols if col in df.columns]

    # Avisar si faltan columnas
    missing = set(expected_cols) - set(service_cols)
    if missing:
        print(f"⚠️ Columnas de servicio no encontradas y omitidas: {missing}")

    if not service_cols:
        print("❌ No hay columnas de servicio disponibles para graficar.")
        return

    # Calcular medias
    mean_scores = df.groupby("satisfaction")[service_cols].mean().T

    fig, ax = plt.subplots(figsize=(12, 6))
    mean_scores.plot(kind="bar", colormap="viridis", ax=ax)

    ax.set_title("Valoración media de servicios por satisfacción")
    ax.set_ylabel("Puntuación media")
    ax.set_xlabel("Servicio")
    plt.xticks(rotation=45)

    plt.tight_layout()
    save_fig(fig, "service_scores_by_satisfaction")
    plt.show()


# ============================================================
# 6. Matriz de correlación
# ============================================================
def plot_correlation_matrix(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include="number")
    corr = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, cmap="coolwarm", annot=False, ax=ax)

    ax.set_title("Matriz de correlación")

    plt.tight_layout()
    save_fig(fig, "correlation_matrix")
    plt.show()


# ============================================================
# 7. Satisfacción por grupo de edad
# ============================================================
def plot_satisfaction_by_age_group(df: pd.DataFrame):
    if "age_group" not in df.columns:
        print("⚠️ La columna 'age_group' no existe. Debes crearla en features.py")
        return

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="age_group",
        hue="satisfaction",
        palette="viridis",
        ax=ax
    )

    ax.set_title("Satisfacción por grupo de edad")
    ax.set_xlabel("Grupo de edad")
    ax.set_ylabel("Cantidad")

    plt.tight_layout()
    save_fig(fig, "satisfaction_by_age_group")
    plt.show()
