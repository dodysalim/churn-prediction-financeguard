"""Configuración del proyecto."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "Churn_Modelling.csv"
TARGET = "Exited"
ID_COLUMNS = ("RowNumber", "CustomerId", "Surname")
TEST_SIZE = 0.2
RANDOM_STATE = 42
CV_FOLDS = 5
