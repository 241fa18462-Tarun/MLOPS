import os
import numpy as np
import joblib
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def train_with_tracking():
    print("[INFO] --- Starting MLflow Experiment Tracking Run ---")

    # 1. Point MLflow at a local, database-backed store.
    #    (A plain file store under ./mlruns does not support the Model
    #    Registry that Lab 6 needs later, so we standardize on sqlite here.)
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("Telco_Churn_Prediction")

    # 2. Load processed data (produced by src/preprocess.py)
    try:
        X_train = np.load('data/processed/X_train_final.npy')
        X_test = np.load('data/processed/X_test_final.npy')
        y_train = np.load('data/processed/y_train.npy')
        y_test = np.load('data/processed/y_test.npy')
    except FileNotFoundError as e:
        print(f"[ERROR] Processed data not found: {e}")
        print("[ERROR] Please run src/preprocess.py first.")
        return

    # 3. Define model parameters (same baseline config as Lab 3,
    #    now captured explicitly so MLflow can log them)
    params = {
        "n_estimators": 100,
        "max_depth": 10,
        "random_state": 42,
        "class_weight": "balanced"
    }

    with mlflow.start_run(run_name="RandomForest_Baseline_Tracked") as run:
        print(f"[INFO] MLflow Run ID: {run.info.run_id}")

        # Log parameters
        mlflow.log_params(params)
        mlflow.log_param("model_family", "RandomForest")

        # 4. Train
        print("[INFO] Training RandomForest model...")
        model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)

        # 5. Evaluate
        print("[INFO] Evaluating model...")
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]

        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred),
            "roc_auc": roc_auc_score(y_test, y_proba)
        }
        mlflow.log_metrics(metrics)

        # 6. Log the model as an MLflow artifact (no registry yet — Lab 6 handles that)
        mlflow.sklearn.log_model(sk_model=model, name="random_forest_model")

        # 7. Also save locally so later steps (and Lab 4's reproducibility
        #    check) can load the exact same artifact without querying MLflow.
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, "models/random_forest_mlflow.pkl")

        # Persist the run id so validate_reproducibility.py can reference this run
        os.makedirs("artifacts", exist_ok=True)
        with open("artifacts/last_mlflow_run_id.txt", "w") as f:
            f.write(run.info.run_id)

        print(f"[SUCCESS] Metrics logged: F1 = {metrics['f1_score']:.4f} | ROC-AUC = {metrics['roc_auc']:.4f}")
        print(f"[SUCCESS] Run '{run.info.run_id}' tracked under experiment 'Telco_Churn_Prediction'")

if __name__ == "__main__":
    train_with_tracking()
