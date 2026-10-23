import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Load model
model = joblib.load("water_model.pkl")

st.title("Water Potability Predictor 💧")
st.write(
    "Enter the water quality parameters below to check if it is safe to"
    " drink."
)

# User inputs
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=7.2)
hardness = st.number_input(
    "Hardness (mg/L)", min_value=0.0, max_value=500.0, value=204.8
)
solids = st.number_input(
    "Solids (ppm)", min_value=0.0, max_value=60000.0, value=22000.0
)
chloramines = st.number_input(
    "Chloramines (ppm)", min_value=0.0, max_value=15.0, value=7.5
)
turbidity = st.number_input(
    "Turbidity (NTU)", min_value=0.0, max_value=10.0, value=4.2
)

if st.button("Check Water Quality"):
  input_data = np.array([[ph, hardness, solids, chloramines, turbidity]])
  prediction = model.predict(input_data)

  if prediction[0] == 1:
    st.success("✅ Result: The water is **Potable** (Safe for consumption).")
  else:
    st.error("❌ Result: The water is **Not Potable** (Unsafe for use).")