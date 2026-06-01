import pandas as pd
def assert_columns(df, columns):
#    Verificamos que el DataFrame contiene todas las columnas necesarias.
    missing = [
        col
        for col in columns
        if col not in df.columns
    ]

    if missing:

        raise ValueError(
            f"Faltan columnas: {missing}\n"
            f" Columnas disponibles: {list(df.columns)}"
        )
    
#    Cargamos y combinamos los datasets de train y test usando rutas definidas en config.py.
def load_data():
    return pd.read_csv(
        r"C:\Users\andyv\OneDrive\Desktop\andy\trabajo Andy\EVOLVE\Data science\python\proyecto\data\processed\clean_airline_passenger_satisfaction.csv"
    )

def kpi_color(value, good_threshold, bad_threshold):
    if value >= good_threshold:
        return "🟢"
    elif value <= bad_threshold:
        return "🔴"
    else:
        return "🟡"