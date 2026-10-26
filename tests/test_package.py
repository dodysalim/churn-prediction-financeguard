"""Pruebas del paquete financeguard."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from financeguard import costs, data, evaluation, features, models  # noqa: E402


@pytest.fixture(scope="module")
def split():
    return data.stratified_split(data.load_dataset())


def test_split_is_stratified_and_drops_ids(split):
    assert len(split.X_train) == 8000 and len(split.X_test) == 2000
    assert not set(data.config.ID_COLUMNS) & set(split.X_train.columns)
    assert abs(split.y_train.mean() - split.y_test.mean()) < 0.005


def test_preprocessing_fits_on_train_only(split):
    X_train, X_test, _ = features.fit_transform(split.X_train, split.X_test)
    assert list(X_train.columns) == list(X_test.columns)
    assert "Geography_Germany" in X_train.columns and "Gender_Male" in X_train.columns
    assert abs(X_train["Age"].mean()) < 1e-9            # escalado con media de train
    assert abs(X_test["Age"].mean()) > 1e-9             # test no se re-ajusta


def test_model_registry():
    assert {"logistic", "random_forest", "xgboost", "xgboost_optimized"} <= set(models.available())
    with pytest.raises(KeyError):
        models.build("inexistente")
    models.register("dummy", lambda spw: "modelo")
    assert models.build("dummy") == "modelo"
    assert models.class_ratio(pd.Series([0, 0, 0, 1])) == 3


def test_logistic_baseline_metrics(split):
    X_train, X_test, _ = features.fit_transform(split.X_train, split.X_test)
    m = evaluation.evaluate(models.build("logistic").fit(X_train, split.y_train), X_test, split.y_test)
    assert 0.75 < m.auc_roc < 0.80
    table = evaluation.comparison_table({"a": m, "b": evaluation.Metrics(0.9, 0.8, 0.7)})
    assert list(table["Model"]) == ["b", "a"]


def test_business_profit_and_threshold():
    c = costs.BusinessCosts()
    assert c.profit(tn=10, fp=2, fn=1, tp=3) == 3 * 450 - 2 * 50 - 500
    y = np.array([0, 0, 1, 1])
    proba = np.array([0.1, 0.4, 0.35, 0.9])
    assert costs.confusion_counts(y, proba, 0.5) == (2, 0, 1, 1)
    t, profit = costs.optimal_threshold(y, proba, thresholds=[0.3, 0.5])
    assert t == 0.3 and profit == 2 * 450 - 50            # capturar ambos churners compensa un FP
