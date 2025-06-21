# 🎬 Netflix Stock Price Predictor Web App

## 📘 Overview
This is an **end-to-end Machine Learning project** that predicts the **future closing price of Netflix stock** using **Lasso Regression**. The project includes all stages of a production ML pipeline: **data preprocessing, feature engineering, model experimentation**, and finally **web deployment** using **Flask**.

The application takes user inputs like Open, High, Low prices and Date (year, month, day), and returns a predicted Close price for that day.

---

## 🚀 Features

- 🧠 **Lasso Regression** model trained on historical stock data
- 🔍 Accepts Open, High, Low prices and future date as input
- 📊 Built-in feature scaling using `StandardScaler`
- 📈 Displays predicted **Close** price with two-decimal precision
- 🖥️ User-friendly **Flask web interface**
- 🎯 Model evaluated using **R² score** for reliability

---

## 🧪 Machine Learning Pipeline

- ✅ **Data Cleaning** – Removed outliers, missing values, and non-numeric entries
- 🛠️ **Feature Engineering** – Extracted year, month, day from date and included price features
- 🔁 **Model Comparison** – Tried multiple regression models
  - Linear Regression
  - Ridge
  - Lasso ✅ *(best performing)*
- 📏 **Evaluation Metric** – Used **R² Score** to evaluate accuracy and avoid overfitting
- 🧠 Final Model: **Lasso Regression**
- 🧃 Output rounded to **2 decimal places** for readability

---

## 🛠️ Technologies Used

| Component         | Technology               |
|-------------------|--------------------------|
| Language          | Python                   |
| Web Framework     | Flask                    |
| ML Model          | Lasso Regression (Scikit-learn) |
| Data Handling     | Pandas, NumPy            |
| Scaling           | StandardScaler           |
| Frontend          | HTML, CSS (Jinja2)       |
| Deployment Ready  | Azure / Render / Heroku  |

---
