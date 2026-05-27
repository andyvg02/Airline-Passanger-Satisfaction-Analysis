import numpy as np
import pandas as pd


def build_features(df) :
    # Retraso total
    df["total_delay"] = (
        df["departure_delay_in_minutes"] +
        df["arrival_delay_in_minutes"]
    )

    # Cliente premium
    df["is_premium_customer"] = np.where(
        (df["customer_type"] == "Loyal Customer") &
        (df["class"].isin(["Business", "Eco Plus"])),
        1,
        0
    )

    # Grupos de edad
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0,18,30,45,60,100],
        labels=["Teen","Young Adult","Adult","Mature","Senior"]
    )

    return df

