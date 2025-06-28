import streamlit as st
import pickle
import numpy as np

# Load the trained Random Forest model
with open("sleep_rf_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit app title and description
st.title("Sleep Quality Predictor")
st.write("Enter your smartphone habits to estimate your sleep quality.")

# Collect user input for each feature
screen_time = st.slider(
    "Screen time (minutes per day)", min_value=0, max_value=600, value=60,
    help="Total time spent using the phone during the day (in minutes)."
)

sleep_duration = st.slider(
    "Sleep duration (minutes)", min_value=0, max_value=900, value=480,
    help="Total time spent sleeping (in minutes)."
)

dark_mode = st.checkbox(
    "Dark mode enabled?", value=False,
    help="Check if you used dark mode on your phone during the evening."
)

# User input -- in the  correct feature order --  as used during training
features = np.array([[screen_time, sleep_duration, int(dark_mode)]])

# When the user clicks the button -> make a prediction & show the result
if st.button("Predict Sleep Quality"):
    predicted_score = model.predict(features)[0]
    st.success(f"Estimated Sleep Quality Score: {predicted_score:.2f} / 10")
