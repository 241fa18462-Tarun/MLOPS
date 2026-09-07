# 🚀 Customer Churn Prediction – MLOps

## 📌 About

This project predicts whether a **telecommunication customer will churn (leave the service)** using Machine Learning.

The project demonstrates basic **MLOps practices** such as data preprocessing, model training, evaluation, model saving, and prediction.

## 📊 Dataset

**Dataset:** Telco Customer Churn

* 7,043 customer records
* 21 columns
* Target: `Churn`
* `Yes` = Customer will churn
* `No` = Customer will not churn

## ⚙️ Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Preprocessing
   ↓
Train/Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Customer Churn Prediction
```

## 🤖 Machine Learning Models

Three models were trained:

1. Logistic Regression
2. Decision Tree
3. Random Forest

## 📈 Results

| Model                   |   Accuracy |   F1 Score |    ROC-AUC |
| ----------------------- | ---------: | ---------: | ---------: |
| **Logistic Regression** | **80.70%** | **60.92%** | **84.16%** |
| Decision Tree           |     79.42% |     58.45% |     82.84% |
| Random Forest           |     77.57% |     60.70% |     82.76% |

🏆 **Best overall model: Logistic Regression**

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib
* Jupyter Notebook
* Git & GitHub

## 📁 Project Structure

```text
MLOPS/
│
├── mlop/
│   └── lab.ipynb
│
├── models/
│   ├── random_forest_churn.pkl
│   └── scaler.pkl
│
└── README.md
```

## 💾 Model Saving

The trained Random Forest model and scaler are saved using **Joblib** so they can be loaded later for prediction.

## 🎯 Objective

The main goal is to identify customers who are likely to churn and help businesses take **early customer-retention actions**.

## 👨‍💻 Author

**Tarun Reddy**

GitHub: `241fa18462-Tarun`
