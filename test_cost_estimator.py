import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("test_cost_estimator_model.pkl")

st.set_page_config(page_title="Medical Test Cost Estimator")
st.title("🧪 Medical Test Cost Estimator")
st.markdown("Estimate the cost of a medical test based on input factors.")

# Form inputs
gender = st.selectbox("Patient Gender", ["Male", "Female"])
age = st.number_input("Patient Age", min_value=0, max_value=120, value=30)
test_type = st.selectbox("Test Type", [
    "Blood Test", "MRI", "CT Scan", "ECG", "X-Ray", "Ultrasound", "Lipid Profile", "Thyroid Panel"
])
insurance_status = st.selectbox("Insurance Status", ["Insured", "Not Insured"])
lab_fee = st.number_input("Lab Service Fee (₹)", min_value=0.0, step=10.0, value=500.0)
preparation_required = st.selectbox("Preparation Required", ["Yes", "No"])
home_sample = st.selectbox("Home Sample Collection", ["Yes", "No"])
urgency_level = st.selectbox("Urgency Level", ["Routine", "Urgent", "Emergency"])

if st.button("Estimate Cost"):
    input_data = pd.DataFrame([{ 
        "gender": gender,
        "age": age,
        "test_type": test_type,
        "insurance_status": insurance_status,
        "lab_service_fee": lab_fee,
        "preparation_required": preparation_required,
        "home_sample_collection": home_sample,
        "urgency_level": urgency_level
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Cost: ₹{prediction:.2f}")
