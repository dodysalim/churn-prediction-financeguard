"""Entrena y compara modelos de churn, y elige el umbral de negocio.

    python train.py                      # comparación + umbral con XGBoost optimizado
    python train.py --models logistic xgboost
"""
import argparse
import sys
from pathlib import Path

from sklearn.model_selection import StratifiedKFold, cross_val_predict

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from financeguard import config, costs, data, evaluation, features, models  # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--models", nargs="+", default=["logistic", "random_forest", "xgboost", "xgboost_optimized"],
                        choices=models.available())
    parser.add_argument("--data", type=Path, default=config.DATA_PATH)
    args = parser.parse_args(argv)

    split = data.stratified_split(data.load_dataset(args.data))
    X_train, X_test, _ = features.fit_transform(split.X_train, split.X_test)
    spw = models.class_ratio(split.y_train)

    results = {}
    for name in args.models:
        model = models.build(name, spw).fit(X_train, split.y_train)
        results[name] = evaluation.evaluate(model, X_test, split.y_test)
    print("\n=== Comparación de modelos (set de prueba, 2.000 clientes) ===")
    print(evaluation.comparison_table(results).to_string(index=False, float_format="%.4f"))

    # Umbral de negocio con XGBoost optimizado y probabilidades out-of-fold de entrenamiento
    best = models.build("xgboost_optimized", spw)
    skf = StratifiedKFold(n_splits=config.CV_FOLDS, shuffle=True, random_state=config.RANDOM_STATE)
    oof = cross_val_predict(models.build("xgboost_optimized", spw), X_train, split.y_train, cv=skf,
                            method="predict_proba")[:, 1]
    threshold, train_profit = costs.optimal_threshold(split.y_train, oof)
    test_proba = best.fit(X_train, split.y_train).predict_proba(X_test)[:, 1]
    print("\n=== Umbral de decisión según costos de retención ===")
    print(f"Umbral óptimo (CV en train): {threshold:.2f} · beneficio en train: ${train_profit:,.2f}")
    print(f"Beneficio en TEST con umbral 0.50: ${costs.profit_at(split.y_test, test_proba, 0.5):,.2f}")
    print(f"Beneficio en TEST con umbral {threshold:.2f}: ${costs.profit_at(split.y_test, test_proba, threshold):,.2f}")
    return results, threshold


if __name__ == "__main__":
    main()
