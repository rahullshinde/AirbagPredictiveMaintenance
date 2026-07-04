import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Dashboard")

if "prediction_result" not in st.session_state:
    st.warning("Please run Prediction first.")
    st.stop()

result = st.session_state["prediction_result"]

st.subheader("Prediction Results")

st.dataframe(result)

healthy = len(result[result["Status"] == "Healthy"])

maintenance = len(
    result[result["Status"] == "Maintenance Required"]
)

col1, col2 = st.columns(2)

col1.metric("Healthy Vehicles", healthy)

col2.metric("Maintenance Required", maintenance)

fig, ax = plt.subplots()

status_counts = result["Status"].value_counts()

ax.pie(
    status_counts,
    labels=status_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Vehicle Health Distribution")

st.pyplot(fig)
