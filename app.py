import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("product_price_estimation_pipeline.pkl")

# Page title
st.title("Product Price Estimation")

st.write(
    "Enter the product details below to predict its price."
)

# User inputs
product_name = st.selectbox(
    "Product Name",
    [
        "Laptop",
        "Smartphone",
        "Mouse",
        "Watch",
        "Backpack",
        "T-shirt",
        "Shoes",
        "Camera",
        "Keyboard",
        "Headphones"
    ]
)

category = st.selectbox(
    "Category",
    ["Electronics", "Fashion"]
)

units_sold = st.number_input(
    "Units Sold",
    min_value=0,
    value=100
)

rating = st.number_input(
    "Rating",
    min_value=0.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)

in_stock = st.selectbox(
    "In Stock",
    [0, 1]
)

# Prediction button
if st.button("Predict Price"):

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "product_name": product_name.lower().strip(),
        "category": category.lower().strip(),
        "units_sold": units_sold,
        "rating": rating,
        "in_stock": in_stock
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    st.success(f"Predicted Product Price: ₹{prediction:.2f}")