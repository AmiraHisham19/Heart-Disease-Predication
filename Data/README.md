## Data

The dataset is the Kaggle *Heart Disease Analysis & Prediction* file. 
It has 303 patients (302 after removing 1 duplicate row), 13 clinical features and a binary target.

The disease group is older, more often male, and has more exercise angina, more ST depression and more blocked vessels.

| Column | Meaning |
|---|---|
| `age`, `sex` | Age in years; sex (1 = male, 0 = female) |
| `cp` | Chest pain type: 0 asymptomatic, 1 atypical angina, 2 non-anginal pain, 3 typical angina |
| `trtbps`, `chol` | Resting blood pressure (mm Hg); serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar > 120 mg/dl (1 = yes) |
| `restecg` | Resting ECG: 0 left ventricular hypertrophy, 1 normal, 2 ST-T wave abnormality |
| `thalachh`, `exng` | Maximum heart rate achieved; exercise-induced angina (1 = yes) |
| `oldpeak`, `slp` | ST depression induced by exercise; slope of the peak exercise ST segment (0 downsloping, 1 flat, 2 upsloping) |
| `caa` | Number of major vessels (0 to 3) colored by fluoroscopy |
| `thall` | Thallium stress test: 1 fixed defect, 2 normal, 3 reversible defect|
| `output` | **Target:** 0 = heart disease, 1 = no heart disease |
