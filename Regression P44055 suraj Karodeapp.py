%%writefile app.py

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'linear_model.pkl'  # Assuming your linear model is saved as 'linear_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a title for your app
st.title("Monthly Revenue Prediction App (Linear Regression)")

# Create input fields for the user to enter the features
st.header("Enter Customer Features:")
feature_names = X.columns.tolist()  # Get feature names from your DataFrame
user_inputs = {}
for feature_name in feature_names:
    user_inputs[feature_name] = st.number_input(feature_name)

# Create a button to trigger the prediction
if st.button("Predict Monthly Revenue"):
    # Create a DataFrame with the user input
    input_data = pd.DataFrame([list(user_inputs.values())], columns=feature_names)

    # Make a prediction using the loaded model
    prediction = loaded_model.predict(input_data)

    # Display the prediction
    st.header("Predicted Monthly Revenue:")
    st.write(prediction[0])