from src.config import TRAIN_PATH, TEST_PATH, OUT_PATH

from src.io import load_data
from src.cleaning import clean_data
from src.features import build_features

from src.utils import assert_columns
from src.viz import plot_graph


def main():

    # Load dataset
    df = load_data(TRAIN_PATH, TEST_PATH)

    # Clean dataset
    df = clean_data(df)

    # Feature engineering
    df = build_features(df)

    # Validate important columns
    assert_columns(
        df,
        [
            "satisfaction",
            "class",
            "total_delay",
            "is_premium_customer",
            "age_group"
        ]
    )

    # Visualization
    plot_graph(df)

    # Create output folder if it doesn't exist
    OUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Export clean dataset
    df.to_csv(
        OUT_PATH,
        index=False
    )

    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
    