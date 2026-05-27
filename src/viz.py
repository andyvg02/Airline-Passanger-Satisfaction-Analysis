import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def plot_graph(df):

    plt.figure(figsize=(8,5))

    sns.countplot(
        data=df,
        x="satisfaction"
    )

    plt.title(
        "Distribución de satisfacción"
    )

    plt.xlabel(
        "Satisfacción"
    )

    plt.ylabel(
        "Cantidad"
    )

    plt.tight_layout()

    plt.show()