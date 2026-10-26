"""Métricas de clasificación y comparación de modelos."""
from dataclasses import asdict, dataclass
from typing import Dict

import pandas as pd
from sklearn.metrics import average_precision_score, f1_score, roc_auc_score


@dataclass(frozen=True)
class Metrics:
    auc_roc: float
    ap_score: float
    f1_score_churn: float


def evaluate(model, X_test, y_test, threshold: float = 0.5) -> Metrics:
    proba = model.predict_proba(X_test)[:, 1]
    pred = model.predict(X_test) if threshold == 0.5 else (proba > threshold).astype(int)
    return Metrics(roc_auc_score(y_test, proba), average_precision_score(y_test, proba),
                   f1_score(y_test, pred, pos_label=1))


def comparison_table(results: Dict[str, Metrics]) -> pd.DataFrame:
    rows = [{"Model": name, "ROC_AUC": m.auc_roc, "AP_Score": m.ap_score, "F1_Score_Churn": m.f1_score_churn}
            for name, m in results.items()]
    return pd.DataFrame(rows).sort_values("F1_Score_Churn", ascending=False).reset_index(drop=True)


def as_dict(m: Metrics) -> dict:
    return asdict(m)
