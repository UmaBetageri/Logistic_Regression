# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xXfVpnfHtA67XRV0YArfNz1ukeRwwjU4
"""

pip install streamlit
pip install joblib

#Creating a Streamlit App

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('logistic_regression_model.pkl')

# Function to make predictions
def predict_survival(Pclass, Age, SibSp, Parch, Fare, Sex_male, Embarked_Q, Embarked_S):
    input_data = np.array([Pclass, Age, SibSp, Parch, Fare, Sex_male, Embarked_Q, Embarked_S]).reshape(1, -1)
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    return prediction, prediction_proba

# Streamlit app
st.title("Titanic Survival Prediction")
st.write("Enter the passenger details to predict the survival probability.")

# User inputs
Pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
Age = st.slider("Age", 0, 80, 29)
SibSp = st.slider("Number of Siblings/Spouses Aboard", 0, 10, 0)
Parch = st.slider("Number of Parents/Children Aboard", 0, 10, 0)
Fare = st.slider("Fare", 0.0, 600.0, 30.0)
Sex = st.selectbox("Sex", ["male", "female"])
Embarked = st.selectbox("Port of Embarkation", ["C = Cherbourg", "Q = Queenstown", "S = Southampton"])

# Convert categorical inputs
Sex_male = 1 if Sex == "male" else 0
Embarked_Q = 1 if Embarked == "Q = Queenstown" else 0
Embarked_S = 1 if Embarked == "S = Southampton" else 0

# Predict button
if st.button("Predict Survival"):
    prediction, prediction_proba = predict_survival(Pclass, Age, SibSp, Parch, Fare, Sex_male, Embarked_Q, Embarked_S)
    survival = "Survived" if prediction[0] == 1 else "Did not survive"
    probability = prediction_proba[0][1] if prediction[0] == 1 else prediction_proba[0][0]
    st.write(f"Prediction: {survival}")
    st.write(f"Survival Probability: {probability:.2f}")

# Display the app
st.write("### Instructions")
st.write("Fill in the passenger details and click 'Predict Survival' to see the prediction.")

