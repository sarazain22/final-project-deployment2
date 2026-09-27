import streamlit as st
import pandas as pd
import pickle

# ==========================================
# LOAD MODEL
# ==========================================

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# ==========================================
# APP
# ==========================================

st.title("Student Performance Prediction")

st.write(
    "Enter the student's information to predict the final grade (G3)."
)


# ==========================================
# INPUTS
# ==========================================

school = st.selectbox(
    "School",
    ["GP", "MS"]
)

age = st.number_input(
    "Age",
    min_value=15,
    max_value=25,
    value=17
)

mjob = st.selectbox(
    "Mother's Job",
    [
        "at_home",
        "health",
        "other",
        "services",
        "teacher"
    ]
)

fjob = st.selectbox(
    "Father's Job",
    [
        "at_home",
        "health",
        "other",
        "services",
        "teacher"
    ]
)

internet = st.selectbox(
    "Internet",
    ["yes", "no"]
)


# ==========================================
# PREDICTION
# ==========================================

if st.button("Predict"):

    input_data = pd.DataFrame({
        "school": [school],
        "age": [age],
        "Mjob": [mjob],
        "Fjob": [fjob],
        "internet": [internet]
    })

    prediction = model.predict(input_data)

    predicted_grade = prediction[0]

    st.success(
        f"Predicted Final Grade (G3): {predicted_grade:.2f}"
    )