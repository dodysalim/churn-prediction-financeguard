"""Matriz de costos de retención y selección del umbral de decisión.

El umbral se elige con probabilidades *out-of-fold* del set de entrenamiento y luego se
aplica una sola vez al set de prueba, para no sobreajustarlo.
"""
from dataclasses import dataclass

import numpy as np
from sklearn.metrics import confusion_matrix


@dataclass(frozen=True)
class BusinessCosts:
    cost_fn: float = 500     # cliente que se va sin ser detectado
    cost_fp: float = 50      # oferta de retención a quien no se iba
    profit_tp: float = 450   # cliente retenido (500 − 50)
    profit_tn: float = 0

    def profit(self, tn: int, fp: int, fn: int, tp: int) -> float:
        return tp * self.profit_tp + tn * self.profit_tn - fp * self.cost_fp - fn * self.cost_fn


def confusion_counts(y_true, proba, threshold: float):
    tn, fp, fn, tp = confusion_matrix(y_true, (np.asarray(proba) > threshold).astype(int), labels=[0, 1]).ravel()
    return int(tn), int(fp), int(fn), int(tp)


def profit_at(y_true, proba, threshold: float, costs: BusinessCosts = BusinessCosts()) -> float:
    return costs.profit(*confusion_counts(y_true, proba, threshold))


def profit_curve(y_true, proba, thresholds=None, costs: BusinessCosts = BusinessCosts()):
    thresholds = np.linspace(0.01, 0.99, 100) if thresholds is None else np.asarray(thresholds)
    return thresholds, np.array([profit_at(y_true, proba, t, costs) for t in thresholds])


def optimal_threshold(y_true, proba, thresholds=None, costs: BusinessCosts = BusinessCosts()):
    """Devuelve (umbral, beneficio) que maximiza el beneficio neto."""
    t, profits = profit_curve(y_true, proba, thresholds, costs)
    i = int(np.argmax(profits))
    return float(t[i]), float(profits[i])
