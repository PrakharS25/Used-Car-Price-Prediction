import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Used Car Price Prediction",
                    page_icon="🚗",
                    layout="wide")

model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")
scaler = joblib.load("scaler.pkl")
brand_model = joblib.load("brand_model.pkl")

st.sidebar.title("🚗 Used Car Price Predictor")

st.sidebar.markdown("---")

st.sidebar.info(
"""
### Model Information

✔ Algorithm
Random Forest Regressor

✔ Accuracy
81%

✔ Features

• Brand

• Model

• Age

• KM Driven

• Transmission

• Owner

• Fuel Type
"""
)

st.markdown("""
# 🚗 Used Car Price Prediction

### Predict the resale value of your car using Machine Learning.

---
""")

st.success("✅ Model Loaded Successfully")

st.subheader("🚘 Enter Car Details...")

left, right = st.columns(2)
with left:
    brand = st.selectbox("Brand", sorted(brand_model.keys()))
    model_name = st.selectbox("Model", brand_model[brand])
    age = st.number_input("Car Age (Years)",min_value=0,max_value=30,value=5,step=1)
    km_driven = st.number_input("Kilometers Driven",min_value=0,value=50000,step=1000)
with right:
    transmission = st.selectbox("Transmission",["Automatic","Manual"])
    owner = st.selectbox("Owner",["first","second","third","fourth","unregistered"])
    fuel = st.selectbox("Fuel Type",["Petrol","Diesel","Hybrid/CNG","hybrid"])

st.write("")
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    predict_button = st.button(
        "🚗 Predict Price",
        use_container_width=True
    )

if predict_button:
    input_data = pd.DataFrame({
        "Brand": [brand],
        "model": [model_name],
        "Age": [age],
        "kmDriven": [km_driven],
        "Transmission": [transmission],
        "Owner": [owner],
        "FuelType": [fuel]
    })

    input_processed = preprocessor.transform(input_data)
    input_scaled = scaler.transform(input_processed)
    prediction = model.predict(input_scaled)

    st.success(f"💰 Estimated Car Price: ₹ {prediction[0]:,.0f}")
    st.balloons()
st.divider()

with st.expander("ℹ️ About this Project"):

    st.markdown("""
### 🚗 Used Car Price Prediction

This project predicts the estimated resale value of a used car
using Machine Learning.

### 🔍 Workflow

- Data Cleaning
- Feature Engineering
- One-Hot Encoding
- Target Encoding
- Feature Scaling
- Model Training
- Model Evaluation
- Streamlit Deployment

### Best Performing Model

Random Forest Regressor

**Accuracy (R² Score): 81%**
    """)

st.divider()

st.caption("Developed by : Prakhar Sharma")