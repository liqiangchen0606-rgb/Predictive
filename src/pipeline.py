"""
End-to-end churn modeling pipeline for the MSIN0097 individual coursework.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.base import ClassifierMixin
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


RANDOM_STATE = 42


@dataclass
class DatasetBundle:
    x_train: pd.DataFrame
    x_val: pd.DataFrame
    x_test: pd.DataFrame
    y_train: pd.Series
    y_val: pd.Series
    y_test: pd.Series


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train churn prediction models.")
    parser.add_argument(
        "--data-path",
        type=Path,
        default=Path("data/raw/Telco-Customer-Churn.csv"),
        help="Path to the Telco churn CSV file.",
    )
    parser.add_argument(
        "--artifacts-dir",
        type=Path,
        default=Path("artifacts"),
        help="Directory where metrics and trained model are saved.",
    )
    return parser.parse_args()


def _build_ohe() -> OneHotEncoder:
    try:
        return OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:
        # Compatibility fallback for older sklearn versions.
        return OneHotEncoder(handle_unknown="ignore", sparse=False)


def load_and_clean_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {path}. Put the Kaggle CSV at this path "
            "or pass --data-path."
        )
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]

    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"].astype(str).str.strip(), errors="coerce"
        )

    if "Churn" not in df.columns:
        raise ValueError("Expected target column 'Churn' in dataset.")

    df["Churn"] = (
        df["Churn"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({"yes": 1, "no": 0, "1": 1, "0": 0, "true": 1, "false": 0})
    )
    if df["Churn"].isna().any():
        bad_values = sorted(df.loc[df["Churn"].isna(), "Churn"].astype(str).unique())
        raise ValueError(f"Could not map all Churn values to 0/1. Bad values: {bad_values}")

    return df


def split_dataset(df: pd.DataFrame) -> DatasetBundle:
    x = df.drop(columns=["Churn"])
    y = df["Churn"].astype(int)

    x_train, x_temp, y_train, y_temp = train_test_split(
        x, y, test_size=0.40, stratify=y, random_state=RANDOM_STATE
    )
    x_val, x_test, y_val, y_test = train_test_split(
        x_temp, y_temp, test_size=0.50, stratify=y_temp, random_state=RANDOM_STATE
    )
    return DatasetBundle(x_train, x_val, x_test, y_train, y_val, y_test)


def build_preprocessor(x_train: pd.DataFrame) -> ColumnTransformer:
    categorical_cols = x_train.select_dtypes(include=["object"]).columns.tolist()
    numerical_cols = x_train.select_dtypes(exclude=["object"]).columns.tolist()

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", _build_ohe()),
        ]
    )
    numerical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    return ColumnTransformer(
        transformers=[
            ("categorical", categorical_transformer, categorical_cols),
            ("numeric", numerical_transformer, numerical_cols),
        ],
        remainder="drop",
    )


def build_models(preprocessor: ColumnTransformer) -> Dict[str, Pipeline]:
    models: Dict[str, ClassifierMixin] = {
        "baseline_dummy": DummyClassifier(strategy="most_frequent"),
        "logistic_regression": LogisticRegression(
            max_iter=2000, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=400,
            max_depth=None,
            min_samples_leaf=2,
            class_weight="balanced_subsample",
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
    }
    return {
        name: Pipeline(steps=[("preprocess", preprocessor), ("model", model)])
        for name, model in models.items()
    }


def evaluate_model(
    model: Pipeline, x_val: pd.DataFrame, y_val: pd.Series
) -> Dict[str, float]:
    y_pred = model.predict(x_val)
    y_proba = model.predict_proba(x_val)[:, 1]
    return {
        "accuracy": float(accuracy_score(y_val, y_pred)),
        "precision": float(precision_score(y_val, y_pred, zero_division=0)),
        "recall": float(recall_score(y_val, y_pred, zero_division=0)),
        "f1": float(f1_score(y_val, y_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_val, y_proba)),
    }


def fit_and_compare(bundle: DatasetBundle) -> Tuple[str, Pipeline, pd.DataFrame]:
    preprocessor = build_preprocessor(bundle.x_train)
    model_map = build_models(preprocessor)
    rows = []
    for name, pipeline in model_map.items():
        pipeline.fit(bundle.x_train, bundle.y_train)
        metrics = evaluate_model(pipeline, bundle.x_val, bundle.y_val)
        rows.append({"model": name, **metrics})

    results = pd.DataFrame(rows).sort_values(
        by=["f1", "roc_auc"], ascending=False
    ).reset_index(drop=True)
    best_name = str(results.iloc[0]["model"])
    best_model = model_map[best_name]
    return best_name, best_model, results


def evaluate_on_test(model: Pipeline, bundle: DatasetBundle) -> Dict[str, object]:
    y_pred = model.predict(bundle.x_test)
    y_proba = model.predict_proba(bundle.x_test)[:, 1]
    return {
        "accuracy": float(accuracy_score(bundle.y_test, y_pred)),
        "precision": float(precision_score(bundle.y_test, y_pred, zero_division=0)),
        "recall": float(recall_score(bundle.y_test, y_pred, zero_division=0)),
        "f1": float(f1_score(bundle.y_test, y_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(bundle.y_test, y_proba)),
        "confusion_matrix": confusion_matrix(bundle.y_test, y_pred).tolist(),
        "classification_report": classification_report(
            bundle.y_test, y_pred, output_dict=True, zero_division=0
        ),
    }


def save_artifacts(
    artifacts_dir: Path,
    comparison: pd.DataFrame,
    best_name: str,
    test_metrics: Dict[str, object],
    model: Pipeline,
) -> None:
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    comparison_path = artifacts_dir / "model_comparison.csv"
    metrics_path = artifacts_dir / "metrics.json"
    model_path = artifacts_dir / "best_model.joblib"

    comparison.to_csv(comparison_path, index=False)
    payload = {
        "best_model": best_name,
        "validation_comparison": comparison.to_dict(orient="records"),
        "test_metrics": test_metrics,
    }
    metrics_path.write_text(json.dumps(payload, indent=2))
    joblib.dump(model, model_path)

    print(f"Saved comparison table: {comparison_path}")
    print(f"Saved metrics summary: {metrics_path}")
    print(f"Saved best model: {model_path}")


def main() -> None:
    args = parse_args()
    raw_df = load_and_clean_data(args.data_path)
    bundle = split_dataset(raw_df)
    best_name, best_model, comparison = fit_and_compare(bundle)
    test_metrics = evaluate_on_test(best_model, bundle)
    save_artifacts(args.artifacts_dir, comparison, best_name, test_metrics, best_model)
    print(f"Selected best model based on validation F1/ROC-AUC: {best_name}")
    print(f"Test F1: {test_metrics['f1']:.4f} | Test ROC-AUC: {test_metrics['roc_auc']:.4f}")


if __name__ == "__main__":
    main()
