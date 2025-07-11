# 🧪 Medical Test Cost Estimator for PathoLab Diagnostics

This project is designed to help **PathoLab Diagnostics** provide transparent cost estimates for medical tests based on various patient and procedural factors. The goal is to empower patients with upfront financial information, aiding in better decision-making and trust.

---

## 🔍 Project Overview

PathoLab Diagnostics offers a wide range of medical testing services. This system uses machine learning to predict the **estimated cost (in INR)** of a test based on:
- Patient demographics (age, gender)
- Type of test
- Insurance status
- Lab service fees
- Preparation requirements
- Home sample collection
- Urgency level

---

## 📁 Project Structure

```
Medical-Test-Cost-Estimator/
├── Medical_Test_Cost_Estimator.ipynb   # Jupyter notebook (model training & evaluation)
├── test_cost_estimator_model.pkl       # Trained machine learning model
├── app.py                              # Streamlit web application
├── Medical Test Cost Estimator.csv     # Dataset used for training
└── README.md                           # Project documentation
```

---

## 🧠 Technologies Used

- **Python** (3.10 recommended)
- **Pandas**, **NumPy**, **Seaborn**, **Matplotlib**
- **scikit-learn** – for preprocessing and model training
- **Random Forest Regressor** – primary regression algorithm
- **Streamlit** – for interactive web interface
- **Joblib** – for model serialization

---

## 🚀 How to Run the Project

### 1. 📦 Install Requirements

Install required libraries using:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib
```

### 2. 🧪 Train the Model (Optional)

Open and run `Medical_Test_Cost_Estimator.ipynb` in Jupyter Notebook or Colab if you want to retrain the model.

### 3. 🌐 Launch the Web App

Run this in your terminal:

```bash
streamlit run test_cost_estimator.py
```

If `streamlit` is not recognized, try:

```bash
python -m streamlit run test_cost_estimator.py
```

---

## 🖥️ Web Interface Features

- Fill in patient and test details
- Click "Estimate Cost"
- Get an instant predicted cost (in INR)