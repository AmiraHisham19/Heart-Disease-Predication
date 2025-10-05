# 🫀 Heart Attack Prediction using Machine Learning
![dataset-cover](visuals/dataset-cover.jpeg)
## ❤️ Why Early Detection Matters

- Cardiovascular diseases are the leading cause of death globally, responsible for **32% of all deaths**.
- Predictive models can flag high-risk individuals **before symptoms appear**, enabling timely intervention and clinical decision support.

---

## 📊 Dataset Overview

Structured tabular dataset with key patient features:

- **Numerical variables**: age, resting blood pressure, cholesterol, chest pain type, etc.
- **Target**: binary classification (presence or absence of heart attack)

---

## 🧠 Workflow Summary

### 🔹 Data Cleaning
- Checked for missing values
- Verified variable types
- Handled duplicates
- Detected outliers using z-scores
<img width="642" height="143" alt="image" src="https://github.com/user-attachments/assets/7e1eca3f-b0c3-468c-9deb-ca9bbff8a33c" />
<img width="242" height="443" alt="image" src="https://github.com/AmiraHisham19/Heart-attack-Predication/blob/ef5ab998e760cbd95ddeab261976f5452e848288/visuals/7.png"  />

### 🔹 Exploratory Data Analysis
- Visualized class balance (heart attack vs. no heart attack)
- Categorized variables into discrete and continuous
- Used histograms and distribution curves to assess skewness
![1](visuals/1.png)![2](visuals/2.png)
![3](visuals/3.png)![4](visuals/4.png)
![5](visuals/5.png)
### 🔹 Feature Engineering
- Applied normalization to ensure equal feature contribution during model learning
<img width="419" height="160" alt="image" src="https://github.com/user-attachments/assets/28d6778b-9b0d-4ea1-abfe-68dabd392c1b" />

### 🔹 Feature Selection
- Retained all features due to correlation with the target
- Used L1 regularization and feature importance methods during modeling

### 🔹 Model Development
- Classification algorithms used:
  - `KNN`, `Logistic Regression`, `Neural Network`, `Random Forest`, `XGBoost`
- Split data into training, validation, and test sets
- Fine-tuned parameters per model

  Logistic Regression
<img width="519" height="260" alt="image" src=https://github.com/AmiraHisham19/Heart-attack-Predication/blob/564c0f2306d6a34dad5d896b0ce125eaa825b488/visuals/download%20(14).png />

<img width="537" height="274" alt="image" src="https://github.com/user-attachments/assets/2c9d0556-ec6b-4f87-933a-f921ef7e4550" />


### 🔹 Model Evaluation
- Focused on **bias-variance tradeoff**, not just high scores
- Metrics: Precision, Recall, F1-Score, Training Time
- Prioritized **Recall** over Precision for clinical relevance:
  - **Recall**: Of all actual heart attack cases, how many did we correctly identify?
  - **Precision**: Of all patients flagged as at risk, how many truly are?

---

## ✅ Results & Insights

- **Best Performing Model**: `XGBoost`
- **Top Predictive Features**:
  - Chest pain type
  - Thalium stress test results
  - Number of major vessels affected

---

## 📁 Project Structure
