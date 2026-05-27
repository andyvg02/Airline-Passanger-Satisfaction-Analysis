from pathlib import Path
import pandas as pd
def load_data(train_path, test_path):

    train = pd.read_csv(train_path, index_col=0)
    test = pd.read_csv(test_path, index_col=0)

    df = pd.concat([train, test], axis=0)

    return df

