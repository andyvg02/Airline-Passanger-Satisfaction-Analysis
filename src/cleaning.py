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

    return df

