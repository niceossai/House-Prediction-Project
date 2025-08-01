import streamlit as st
import pickle
import numpy as np
import joblib

# Load the model
with open("model.pkl", "rb") as file:
    model =joblib.load("model.pkl")

st.set_page_config(page_title="House Price Prediction", layout="centered")
st.title("🏠 House Price Prediction App")
st.markdown("Enter the details of the house below to predict the **price**:")

# Numeric inputs
area = st.number_input("Area (sq ft)", min_value=100.0, step=10.0, value=500.0)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, step=1, value=2)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, step=1, value=1)
stories = st.number_input("Number of Stories", min_value=1, step=1, value=1)
parking = st.number_input("Number of Parking Spaces", min_value=0, step=1, value=1)

# Binary categorical inputs
mainroad = st.radio("Is it on the main road?", ["Yes", "No"])
guestroom = st.radio("Guest Room Available?", ["Yes", "No"])
basement = st.radio("Basement Available?", ["Yes", "No"])
hotwaterheating = st.radio("Hot Water Heating?", ["Yes", "No"])
airconditioning = st.radio("Air Conditioning?", ["Yes", "No"])
prefarea = st.radio("Is it in a preferred area?", ["Yes", "No"])

# Convert categorical to one-hot encoding
def binary_encoding(option):
    return [1, 0] if option == "Yes" else [0, 1]

# Create input vector (17 features, no price placeholder)
input_data = [
    area,
    bedrooms,
    bathrooms,
    stories,
    parking,
    *binary_encoding(mainroad),
    *binary_encoding(guestroom),
    *binary_encoding(basement),
    *binary_encoding(hotwaterheating),
    *binary_encoding(airconditioning),
    *binary_encoding(prefarea)
]

# Prediction
if st.button("Predict Price"):
    prediction = model.predict([input_data])[0]
    st.success(f"💰 Estimated House Price: $ {prediction:,.2f}")
