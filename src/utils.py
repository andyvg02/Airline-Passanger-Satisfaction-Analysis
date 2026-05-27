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