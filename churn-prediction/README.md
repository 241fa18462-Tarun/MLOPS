# 🚀 Customer Churn Prediction – MLOps

## 📌 About

This project predicts whether a **telecommunication customer will churn (leave the service)** using Machine Learning.

The project demonstrates MLOps practices such as:

- Data preprocessing
- Model training
- Model evaluation
- MLflow experiment tracking
- Reproducibility checking
- Production data pipeline
- Model Registry
- Model lifecycle management

## 📊 Dataset

**Dataset:** Telco Customer Churn

- 7,043 customer records
- Target: `Churn`
- `Yes` = Customer will churn
- `No` = Customer will not churn

## ⚙️ Workflow

```text
Dataset
   ↓
Data Validation
   ↓
Data Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
MLflow Tracking
   ↓
Reproducibility Validation
   ↓
Production Pipeline
   ↓
Model Registry
   ↓
Staging
   ↓
Production
```

## 🤖 Machine Learning Model

The project uses a **Random Forest** model for customer churn prediction.

## 📈 Results

Example results from the pipeline:

| Metric | Result |
|---|---:|
| Accuracy | 75.59% |
| Precision | 52.76% |
| Recall | 76.74% |
| F1 Score | 62.53% |
| ROC-AUC | 84.33% |

## 🧪 MLOps Labs

### Lab 3 – Baseline ML Pipeline

Performs preprocessing, model training, and evaluation.

```powershell
python .\pipelines\run_lab3_baseline.py
```

### Lab 4 – MLflow Tracking

Tracks experiments, metrics, and validates reproducibility.

```powershell
python .\pipelines\run_lab4_tracking.py
```

### Lab 5 – Production Data Pipeline

Validates the dataset and creates the production preprocessing pipeline.

```powershell
python .\pipelines\run_lab5_pipeline.py
```

### Lab 6 – Model Registry

Registers the trained model and manages the model lifecycle.

```powershell
python .\pipelines\run_lab6_registry.py
```

# ▶️ How to Run

Open PowerShell in the project folder.

```powershell
cd .\churn-prediction
```

Check the files:

```powershell
dir
```

View the project structure:

```powershell
tree /F
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

Then run the pipelines in order.

---

# 🧪 Example Output

## Lab 3 – Baseline ML Pipeline

Run:

```powershell
python .\pipelines\run_lab3_baseline.py
```

Example:

```text
PS C:\Users\ASUS\OneDrive\Desktop\churn-prediction\churn-prediction> python .\pipelines\run_lab3_baseline.py

[INFO] =========================================
[INFO] Starting Lab 3: Baseline ML Pipeline
[INFO] =========================================

[INFO] ---> Executing src/preprocess.py...
Starting Preprocessing Pipeline...
Preprocessing completed successfully!

[INFO] ---> Executing src/train.py...
Starting Model Training...
Model training complete and saved to disk!

[INFO] ---> Executing src/evaluate.py...
Starting Model Evaluation...

--- Model Evaluation Report ---
Accuracy : 0.7559
Precision: 0.5276
Recall   : 0.7674
F1-Score : 0.6253
-------------------------------

Evaluation complete and error analysis files saved!

[SUCCESS] Lab 3 Pipeline fully executed!
```

---

## Lab 4 – MLflow Experiment Tracking

Run:

```powershell
python .\pipelines\run_lab4_tracking.py
```

Example:

```text
PS C:\Users\ASUS\OneDrive\Desktop\churn-prediction\churn-prediction> python .\pipelines\run_lab4_tracking.py

[INFO] =========================================
[INFO] Starting Lab 4: MLflow Experiment Tracking
[INFO] =========================================

[INFO] ---> Executing src/preprocess.py...
Starting Preprocessing Pipeline...
Preprocessing completed successfully!

[INFO] ---> Executing src/train_mlflow.py...
[INFO] --- Starting MLflow Experiment Tracking Run ---

[INFO] MLflow Run ID: e5e8110395cc4a9dabd1f0caae412367
[INFO] Training RandomForest model...
[INFO] Evaluating model...

[SUCCESS] Metrics logged: F1 = 0.6253 | ROC-AUC = 0.8433

[SUCCESS] Run tracked under experiment 'Telco_Churn_Prediction'

[INFO] ---> Executing src/validate_reproducibility.py...
[INFO] --- Validating Training Reproducibility ---

[INFO] Training run A...
[INFO] Training run B...

[SUCCESS] Reproducibility Validation PASSED.
[INFO] Model training is fully deterministic given the same seed and data.

[SUCCESS] Lab 4 Pipeline fully executed!
```

---

## Lab 5 – Production Data Pipeline

Run:

```powershell
python .\pipelines\run_lab5_pipeline.py
```

Example:

```text
PS C:\Users\ASUS\OneDrive\Desktop\churn-prediction\churn-prediction> python .\pipelines\run_lab5_pipeline.py

[INFO] =========================================
[INFO] Starting Lab 5: Production Data Pipeline
[INFO] =========================================

[INFO] ---> Executing src/validate_data.py...
[INFO] Validating schema (Records: 7044)...
[SUCCESS] Schema Validation PASSED. Dataset is clean.

[INFO] ---> Executing src/preprocess_pipeline.py...
[INFO] Starting Sklearn Pipeline Preprocessing...
[INFO] Fitting and transforming training data...
[INFO] Transforming test data...

[SUCCESS] Preprocessing completed successfully!
Pipeline saved as preprocessor.pkl.

[INFO] ---> Executing src/validate_outputs.py...
[INFO] Validating Preprocessing Outputs...

[SUCCESS] Output Validation PASSED.
[INFO] Features are clean, scaled, encoded, and dimensionally consistent.

[INFO] Summary report saved to artifacts/preprocessing_summary_report.json

[SUCCESS] Lab 5 Production Pipeline fully executed!
```

---

## Lab 6 – Model Registry & Lifecycle

Run:

```powershell
python .\pipelines\run_lab6_registry.py
```

Example:

```text
PS C:\Users\ASUS\OneDrive\Desktop\churn-prediction\churn-prediction> python .\pipelines\run_lab6_registry.py

[INFO] =========================================
[INFO] Starting Lab 6: Model Registry & Lifecycle
[INFO] =========================================

[INFO] ---> Executing src/train_registry.py...
[INFO] --- Starting MLflow Run with Model Registry ---

[INFO] Training RandomForest model...
[INFO] Evaluating model...
[INFO] Attaching preprocessing pipeline to model artifacts...
[INFO] Pushing model to MLflow Registry...

Successfully registered model 'Telco_Churn_Production_Model'.
Created version '1' of model 'Telco_Churn_Production_Model'.

[SUCCESS] Metrics logged: F1 = 0.6179 | ROC-AUC = 0.8321

[SUCCESS] Model successfully registered under name:
'Telco_Churn_Production_Model'

[INFO] ---> Executing src/automate_lifecycle.py...
[INFO] Starting Automated Model Lifecycle Manager...

[INFO] Found 1 new model(s). Moving them to Staging...

-> Version 1 is now in Staging.

[INFO] Evaluating Staging candidates...
-> Staging Candidate: Version 1 | recall: 0.7005

[INFO] Promoting Version 1 to Production...

[SUCCESS] Automated Model Lifecycle execution complete!

[INFO] ---> Executing src/generate_registry_report.py...
[INFO] Generating Model Registry Report...

[SUCCESS] Report successfully generated for Version 1
[SUCCESS] Saved to: artifacts/production_model_report.json

[SUCCESS] Lab 6 Model Registry Pipeline fully executed!
```

> **Note:** MLflow may show a `FutureWarning` about model registry stages being deprecated. This is a warning from MLflow and does not mean the pipeline failed.

---

## 📁 Project Structure

```text
churn-prediction/
│
├── artifacts/
│
├── data/
│   ├── processed/
│   └── raw/
│       └── churn.csv
│
├── logs/
│
├── models/
│
├── notebooks/
│   └── project_implementation.ipynb
│
├── outputs/
│
├── pipelines/
│   ├── run_lab3_baseline.py
│   ├── run_lab4_tracking.py
│   ├── run_lab5_pipeline.py
│   └── run_lab6_registry.py
│
├── src/
│   ├── automate_lifecycle.py
│   ├── evaluate.py
│   ├── generate_registry_report.py
│   ├── preprocess.py
│   ├── preprocess_pipeline.py
│   ├── train.py
│   ├── train_mlflow.py
│   ├── train_registry.py
│   ├── validate_data.py
│   ├── validate_outputs.py
│   └── validate_reproducibility.py
│
├── .gitignore
└── requirements.txt
```

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- MLflow
- Random Forest
- Jupyter Notebook
- Git
- GitHub

## 📦 MLflow

MLflow is used for:

- Experiment tracking
- Metric logging
- Model registration
- Model versioning
- Model lifecycle management

Registered model:

```text
Telco_Churn_Production_Model
```

## 🎯 Objective

The main goal is to build a complete MLOps workflow for **customer churn prediction**, from data preparation and model training to model tracking, registration, and production lifecycle management.

## 👨‍💻 Author

**Tarun Reddy**

GitHub: `241fa18462-Tarun`
