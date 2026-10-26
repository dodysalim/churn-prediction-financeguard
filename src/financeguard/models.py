"""Registro de modelos de clasificación (fábrica abierta a extensión).

Cada entrada recibe `scale_pos_weight` (negativos/positivos) para compensar el desbalance.
Para sumar un modelo basta con `register("nombre", constructor)`.
"""
from typing import Callable, Dict

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from financeguard import config

Builder = Callable[[float], object]
_REGISTRY: Dict[str, Builder] = {}

# Mejores hiperparámetros de XGBoost hallados con GridSearchCV (notebook 2)
BEST_XGB_PARAMS = dict(n_estimators=150, learning_rate=0.05, max_depth=7, subsample=0.7,
                       colsample_bytree=0.7, gamma=0, objective='binary:logistic')


def register(name: str, builder: Builder) -> None:
    _REGISTRY[name] = builder


def available() -> list:
    return list(_REGISTRY)


def build(name: str, scale_pos_weight: float = 1.0):
    if name not in _REGISTRY:
        raise KeyError(f"Modelo '{name}' no registrado. Disponibles: {available()}")
    return _REGISTRY[name](scale_pos_weight)


def class_ratio(y: pd.Series) -> float:
    counts = y.value_counts()
    return counts[0] / counts[1]


def _xgb(**params):
    def make(spw):
        import xgboost as xgb
        return xgb.XGBClassifier(random_state=config.RANDOM_STATE, n_jobs=-1, scale_pos_weight=spw, **params)
    return make


register("logistic", lambda spw: LogisticRegression(random_state=config.RANDOM_STATE, solver='liblinear',
                                                    class_weight='balanced'))
register("random_forest", lambda spw: RandomForestClassifier(n_estimators=200, max_depth=10, n_jobs=-1,
                                                             random_state=config.RANDOM_STATE,
                                                             class_weight='balanced'))
register("xgboost", _xgb(n_estimators=200, learning_rate=0.1, max_depth=5, subsample=0.8, colsample_bytree=0.8,
                         gamma=0.1, objective='binary:logistic'))
register("xgboost_optimized", _xgb(**BEST_XGB_PARAMS))
