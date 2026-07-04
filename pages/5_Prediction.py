import streamlit as st
import joblib
import pandas as pd

st.title("🔍 Prediction")

if "processed_data" not in st.session_state:
    st.warning("Please preprocess the data first.")
    st.stop()

model = joblib.load("model/model.pkl")

if st.button("Predict"):

    df = st.session_state["processed_data"]

    # Predict all rows
    predictions = model.predict(df)

    # Probability for all rows
    probabilities = model.predict_proba(df)

    # Create result dataframe
    result = df.copy()

    result["Status"] = [
        "Maintenance Required" if p == 1 else "Healthy"
        for p in predictions
    ]

    result["Confidence (%)"] = [
        round(max(prob) * 100, 2)
        for prob in probabilities
    ]

    # Save for dashboard
    st.session_state["prediction_result"] = result

    st.success("Prediction completed successfully!")

    st.dataframe(result)
