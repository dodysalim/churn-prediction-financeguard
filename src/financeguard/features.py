"""Preprocesamiento: escalado de numéricas y one-hot de categóricas (sin fuga de información)."""
from typing import List, Tuple

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def feature_types(X: pd.DataFrame) -> Tuple[List[str], List[str]]:
    return X.select_dtypes(include=np.number).columns.tolist(), X.select_dtypes(include='object').columns.tolist()


def build_preprocessor(numeric: List[str], categorical: List[str]) -> ColumnTransformer:
    return ColumnTransformer([
        ('num', StandardScaler(), numeric),
        ('cat', OneHotEncoder(handle_unknown='ignore', drop='first'), categorical),
    ])


def fit_transform(X_train: pd.DataFrame, X_test: pd.DataFrame):
    """Ajusta el preprocesador solo con entrenamiento y devuelve DataFrames con nombres legibles."""
    numeric, categorical = feature_types(X_train)
    pre = build_preprocessor(numeric, categorical)
    train = pre.fit_transform(X_train)
    test = pre.transform(X_test)
    names = numeric + list(pre.named_transformers_['cat'].get_feature_names_out(categorical))
    return (pd.DataFrame(train, columns=names, index=X_train.index),
            pd.DataFrame(test, columns=names, index=X_test.index), pre)
