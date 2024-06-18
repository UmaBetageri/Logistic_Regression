# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xXfVpnfHtA67XRV0YArfNz1ukeRwwjU4
"""

import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Titanic Survival Prediction")
st.write("Enter the details to predict survival:")

# Input fields for the features
pclass = st.selectbox("Pclass", [1, 2, 3])
age = st.number_input("Age", value=0.0)
sibsp = st.number_input("SibSp", value=0)
parch = st.number_input("Parch", value=0)
fare = st.number_input("Fare", value=0.0)
sex = st.selectbox("Sex", ["Male", "Female"])
embarked = st.selectbox("Embarked", ["C", "Q", "S"])

# Convert categorical inputs to numerical
sex_male = 1 if sex == "Male" else 0
embarked_Q = 1 if embarked == "Q" else 0
embarked_S = 1 if embarked == "S" else 0

# Button for prediction
if st.button("Predict"):
    features = np.array([[pclass, age, sibsp, parch, fare, sex_male, embarked_Q, embarked_S]])
    prediction = model.predict(features)
    prediction_proba = model.predict_proba(features)

    if prediction[0] == 1:
        st.write("Prediction: Survived")
    else:
        st.write("Prediction: Did not survive")

    st.write(f"Probability of Survival: {prediction_proba[0][1]:.2f}")
    st.write(f"Probability of Not Surviving: {prediction_proba[0][0]:.2f}")

