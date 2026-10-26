"""Integridad del dataset y ejecución de notebooks rápidos."""
from pathlib import Path

import nbformat
import pandas as pd
import pytest
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "Churn_Modelling.csv"


def test_dataset_shape_and_target():
    df = pd.read_csv(DATA)
    assert len(df) == 10_000
    assert {"CreditScore", "Geography", "Age", "Balance", "Exited"}.issubset(df.columns)
    assert set(df["Exited"].unique()) == {0, 1}
    assert df["CustomerId"].is_unique


@pytest.mark.parametrize("name", ["1_EDA_RegresionLogistica.ipynb", "4_Extra_credit.ipynb"])
def test_notebook_executes(name):
    nb = nbformat.read(ROOT / "notebooks" / name, as_version=4)
    NotebookClient(nb, timeout=600, kernel_name="python3",
                   resources={"metadata": {"path": str(ROOT / "notebooks")}}).execute()
