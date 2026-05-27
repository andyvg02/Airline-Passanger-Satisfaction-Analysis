import pandas as pd


def clean_data(df):

    # Renombrar columnas
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
    )

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Nulos
    df["arrival_delay_in_minutes"] = (
        df["arrival_delay_in_minutes"]
        .fillna(df["arrival_delay_in_minutes"].median())
    )
    # Convertir columnas categóricas
    categorical_cols = [
        "gender",
        "customer_type",
        "type_of_travel",
        "class",
        "satisfaction"
    ]

    for col in categorical_cols:
        df[col] = df[col].astype("category")
    
    return df

