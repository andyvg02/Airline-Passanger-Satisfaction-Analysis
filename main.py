from src.config import TRAIN_PATH, TEST_PATH, OUT_PATH

from src.io import load_data
from src.cleaning import clean_data
from src.features import build_features
from src.utils import assert_columns

from src.viz import (
    plot_satisfaction_distribution,
    plot_satisfaction_by_class,
    plot_satisfaction_by_customer_type,
    plot_delay_by_satisfaction,
    plot_service_scores_by_satisfaction,
    plot_correlation_matrix,
    plot_satisfaction_by_age_group
)


def main():

    print("\n📥 Cargando dataset...")
    df = load_data(TRAIN_PATH, TEST_PATH)

    print("🧹 Limpiando datos...")
    df = clean_data(df)

    print("🧪 Generando nuevas características...")
    df = build_features(df)

    print("🔍 Validando columnas esenciales...")
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

    print("\n📊 Generando visualizaciones...")
    plot_satisfaction_distribution(df)
    plot_satisfaction_by_class(df)
    plot_satisfaction_by_customer_type(df)
    plot_delay_by_satisfaction(df)
    plot_service_scores_by_satisfaction(df)
    plot_correlation_matrix(df)
    plot_satisfaction_by_age_group(df)

    print("\n💾 Guardando dataset limpio...")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print(f"✅ Dataset guardado en: {OUT_PATH}")


if __name__ == "__main__":
    main()