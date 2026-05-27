import pandas as pd
def assert_columns(df, columns):

    missing = [
        col
        for col in columns
        if col not in df.columns
    ]

    if missing:

        raise ValueError(
            f"Faltan columnas: {missing}"
        )