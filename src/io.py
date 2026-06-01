from pathlib import Path
import pandas as pd


def load_data(train_path: Path, test_path: Path) -> pd.DataFrame:
    """
    Carga y combina los datasets de train y test.

    Parámetros
    ----------
    train_path : Path
        Ruta al archivo train.csv
    test_path : Path
        Ruta al archivo test.csv

    Retorna
    -------
    pd.DataFrame
        DataFrame combinado sin asumir índices ni columnas especiales.
    """

    # Validación de existencia de archivos
    if not train_path.exists():
        raise FileNotFoundError(f"❌ No se encontró el archivo: {train_path}")

    if not test_path.exists():
        raise FileNotFoundError(f"❌ No se encontró el archivo: {test_path}")

    # Carga segura sin asumir index_col
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)

    # Concatenación robusta
    df = pd.concat([train, test], ignore_index=True)

    return df