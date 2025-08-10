import pickle
import numpy as np
import streamlit as st






# Load model
model = pickle.load(open('heart_model.sav', 'rb'))

st.title("❤️ Heart Disease Prediction App")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", (0, 1))  # 0 = female, 1 = male
cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, value=0)
trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=250, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", (0, 1))
restecg = st.number_input("Resting ECG results (0-2)", min_value=0, max_value=2, value=1)
thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina", (0, 1))
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
slope = st.number_input("Slope (0-2)", min_value=0, max_value=2, value=1)
ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0)
thal = st.number_input("Thal (0-3)", min_value=0, max_value=3, value=1)

# Prediction
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                             exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.success("✅ Person does NOT have Heart Disease")
    else:
        st.error("⚠️ Person HAS Heart Disease")
