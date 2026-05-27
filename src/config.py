from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TRAIN_PATH = ROOT / "data" / "raw" / "train.csv"
TEST_PATH = ROOT / "data" / "raw" / "test.csv"

OUT_PATH = ROOT / "data" / "processed" / "clean_airline_passenger_satisfaction.csv"

