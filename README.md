🏦 Credit Risk Modelling - ML App (End-to-End)
This project is an end-to-end machine learning application that predicts the likelihood of a loan applicant defaulting on credit. It's designed to help financial institutions make informed lending decisions. The application is built using Python, Scikit-learn/XGBoost, and Streamlit for deployment.

💡 Problem Statement
The objective is to classify loan applications as:

Risky (label = 1) – High likelihood of default

Safe (label = 0) – Low likelihood of default

By analyzing applicants’ financial, employment, and demographic data, this model can assist banks and credit providers in mitigating loan default risk.

🔍 Features
📊 Exploratory Data Analysis (EDA)
Visualize distributions, relationships, and detect imbalance or outliers.

🧹 Data Preprocessing

Handling missing values

Feature engineering

Encoding categorical variables

Scaling/normalization

📦 Model Training

XGBoost

Logistic Regression

Random Forest

Hyperparameter tuning with GridSearchCV

✅ Model Evaluation

Confusion Matrix

Precision, Recall, F1-Score

ROC-AUC Curve

SHAP Value Interpretability

💾 Model & Scaler Saving

model.pkl

scaler.pkl

🖥️ Streamlit App Deployment
Interactive frontend for inputting applicant details and receiving prediction results.

🔐 Secrets & Credential Management

.env file

Azure Key Vault (optional for production)

📷 Final Streamlit App Output 
(Comming soon)

🧪 Example Use Cases
Banks determining eligibility of personal or business loans
Credit Bureaus evaluating customer risk profile
FinTech platforms streamlining loan approvals with automation 

🗂️ Version Control Steps (Git)
# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Initial commit - Credit Risk Modelling"

# Link to remote (if not already)
git remote add origin <your-repo-url>

# Push to main branch
git push -u origin main

# Pull before next push to avoid conflicts
git pull origin main --rebase

# Create a feature branch
git checkout -b feature-branch

# Merge to main
git checkout main
git merge feature-branch

⚠️ Disclaimer
This project is developed solely for educational and demonstration purposes.
The dataset used is fictitious. No real individuals, identities, or financial records are associated with this model.Please do not use this application for real-world credit approval decisions.



