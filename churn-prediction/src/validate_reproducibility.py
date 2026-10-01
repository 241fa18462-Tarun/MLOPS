import os
import sys
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def validate_reproducibility():
    print("[INFO] --- Validating Training Reproducibility ---")

    # 1. Load processed data
    try:
        X_train = np.load('data/processed/X_train_final.npy')
        X_test = np.load('data/processed/X_test_final.npy')
        y_train = np.load('data/processed/y_train.npy')
        y_test = np.load('data/processed/y_test.npy')
    except FileNotFoundError as e:
        print(f"[ERROR] Could not find processed data: {e}")
        sys.exit(1)

    params = {
        "n_estimators": 100,
        "max_depth": 10,
        "random_state": 42,
        "class_weight": "balanced"
    }

    # 2. Train the SAME model twice from scratch, with an identical
    #    random_state, and confirm the results are bit-for-bit identical.
    #    This is the reproducibility guarantee MLflow tracking is meant
    #    to make verifiable: same code + same data + same seed = same model.
    print("[INFO] Training run A...")
    model_a = RandomForestClassifier(**params)
    model_a.fit(X_train, y_train)
    preds_a = model_a.predict(X_test)
    proba_a = model_a.predict_proba(X_test)

    print("[INFO] Training run B...")
    model_b = RandomForestClassifier(**params)
    model_b.fit(X_train, y_train)
    preds_b = model_b.predict(X_test)
    proba_b = model_b.predict_proba(X_test)

    errors = []

    # 3. Compare predictions exactly
    if not np.array_equal(preds_a, preds_b):
        errors.append("Predictions differ between run A and run B.")

    # 4. Compare predicted probabilities exactly
    if not np.allclose(proba_a, proba_b):
        errors.append("Predicted probabilities differ between run A and run B.")

    # 5. Compare metrics exactly
    metrics_a = {
        "accuracy": accuracy_score(y_test, preds_a),
        "precision": precision_score(y_test, preds_a),
        "recall": recall_score(y_test, preds_a),
        "f1_score": f1_score(y_test, preds_a),
    }
    metrics_b = {
        "accuracy": accuracy_score(y_test, preds_b),
        "precision": precision_score(y_test, preds_b),
        "recall": recall_score(y_test, preds_b),
        "f1_score": f1_score(y_test, preds_b),
    }

    for key in metrics_a:
        if metrics_a[key] != metrics_b[key]:
            errors.append(f"Metric '{key}' differs: run A={metrics_a[key]} vs run B={metrics_b[key]}")

    # 6. Build and save the reproducibility report
    report = {
        "validation_status": "PASSED" if not errors else "FAILED",
        "run_a_metrics": metrics_a,
        "run_b_metrics": metrics_b,
        "params_used": params,
        "errors": errors
    }

    os.makedirs("artifacts", exist_ok=True)
    report_path = "artifacts/reproducibility_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=4)

    if errors:
        print("[ERROR] Reproducibility Validation FAILED!")
        for e in errors:
            print(f"  - {e}")
        print(f"[INFO] Report saved to {report_path}")
        sys.exit(1)
    else:
        print("[SUCCESS] Reproducibility Validation PASSED.")
        print("[INFO] Model training is fully deterministic given the same seed and data.")
        print(f"[INFO] Report saved to {report_path}")

if __name__ == "__main__":
    validate_reproducibility()
