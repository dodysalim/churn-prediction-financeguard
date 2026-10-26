"""Carga del dataset y partición estratificada entrenamiento/prueba."""
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from financeguard import config


@dataclass(frozen=True)
class Split:
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series


def load_dataset(path: Path = config.DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def drop_identifiers(df: pd.DataFrame) -> pd.DataFrame:
    """Quita columnas que identifican al cliente pero no lo describen."""
    return df.drop(columns=[c for c in config.ID_COLUMNS if c in df.columns])


def features_and_target(df: pd.DataFrame):
    clean = drop_identifiers(df)
    return clean.drop(columns=config.TARGET), clean[config.TARGET]


def stratified_split(df: pd.DataFrame, test_size: float = config.TEST_SIZE,
                     random_state: int = config.RANDOM_STATE) -> Split:
    X, y = features_and_target(df)
    return Split(*train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y))
