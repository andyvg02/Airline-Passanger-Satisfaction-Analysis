import pandas as pd


def clean_data(df):
    """
    Limpia y prepara el dataset de satisfacción de pasajeros.

    Pasos:
    - Normaliza nombres de columnas
    - Elimina duplicados
    - Imputa nulos en arrival_delay_in_minutes
    - Convierte columnas categóricas
    - Asegura consistencia en valores categóricos

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame original cargado desde train + test.

    Returns
    -------
    pd.DataFrame
        DataFrame limpio y listo para feature engineering.
    """
    # Renombrar columnas
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Imputación de nulos
    if "arrival_delay_in_minutes" in df.columns:
        df["arrival_delay_in_minutes"] = df["arrival_delay_in_minutes"].fillna(
            df["arrival_delay_in_minutes"].median()
        )

        # Asegurar que no haya delays negativos
        df["arrival_delay_in_minutes"] = df["arrival_delay_in_minutes"].clip(lower=0)

    # Columnas categóricas
    categorical_cols = [
        "gender",
        "customer_type",
        "type_of_travel",
        "class",
        "satisfaction"
    ]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype("category")
    return df

