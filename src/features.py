import numpy as np
import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Construye nuevas características para el análisis y modelado.

    Features creadas:
    - total_delay: suma de departure + arrival delay
    - is_premium_customer: cliente leal + clase alta
    - age_group: grupos de edad categorizados y ordenados

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame limpio tras cleaning.py

    Returns
    -------
    pd.DataFrame
        DataFrame con nuevas columnas de features.
    """

    # -----------------------------
    # 1. Retraso total
    # -----------------------------
    if {"departure_delay_in_minutes", "arrival_delay_in_minutes"}.issubset(df.columns):
        df["total_delay"] = (
            df["departure_delay_in_minutes"].clip(lower=0) +
            df["arrival_delay_in_minutes"].clip(lower=0)
        )
    else:
        raise KeyError("Faltan columnas de delay para crear total_delay")

    # -----------------------------
    # 2. Cliente premium
    # -----------------------------
    if {"customer_type", "class"}.issubset(df.columns):

        # Normalizar valores por seguridad
        df["customer_type"] = df["customer_type"].str.title()
        df["class"] = df["class"].str.title()

        df["is_premium_customer"] = np.where(
            (df["customer_type"] == "Loyal Customer") &
            (df["class"].isin(["Business", "Eco Plus"])),
            1,
            0
        )
    else:
        raise KeyError("Faltan columnas customer_type o class para crear is_premium_customer")

    # -----------------------------
    # 3. Grupos de edad
    # -----------------------------
    if "age" in df.columns:
        df["age_group"] = pd.cut(
            df["age"].clip(lower=0, upper=100),
            bins=[0, 18, 30, 45, 60, 120],
            labels=["Teen", "Young Adult", "Adult", "Mature", "Senior"],
            include_lowest=True
        )

        # Convertir a categoría ordenada
        df["age_group"] = df["age_group"].astype(
            pd.CategoricalDtype(
                categories=["Teen", "Young Adult", "Adult", "Mature", "Senior"],
                ordered=True
            )
        )
    else:
        raise KeyError("La columna age es necesaria para crear age_group")

    return df