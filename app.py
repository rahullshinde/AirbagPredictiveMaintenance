import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Predictive Maintenance for Airbag Systems",
    page_icon="🚗",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("🚗 Predictive Maintenance for Automotive Airbag Systems")
st.markdown("---")

# --------------------------------------------------
# Project Overview
# --------------------------------------------------
st.header("📌 Project Overview")

st.write("""
Airbag systems are one of the most critical safety components in modern vehicles.
Traditional maintenance relies on scheduled servicing or warning indicators,
which may fail to detect degrading components before they become unsafe.

This application uses **Machine Learning** to predict whether an automotive
airbag system requires preventive maintenance by analyzing vehicle diagnostics
and historical maintenance data.
""")

# --------------------------------------------------
# Objectives
# --------------------------------------------------
st.header("🎯 Objectives")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    ✔ Predict airbag system failures

    ✔ Recommend preventive maintenance

    ✔ Reduce unexpected airbag failures

    ✔ Improve passenger safety
    """)

with col2:
    st.info("""
    ✔ Improve maintenance planning

    ✔ Reduce maintenance cost

    ✔ Support technicians

    ✔ Demonstrate ML-based software architecture
    """)

# --------------------------------------------------
# Selected ML Algorithm
# --------------------------------------------------
st.header("🤖 Machine Learning Model")

st.write("""
**Algorithm:** Random Forest Classifier

Why Random Forest?

- High prediction accuracy
- Handles noisy automotive sensor data
- Easy to interpret
- Robust against overfitting
- Provides feature importance
""")

# --------------------------------------------------
# Architecture
# --------------------------------------------------
st.header("🏗️ Selected Architecture")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Pipe-and-Filter")

    st.write("""
    Data flows through independent processing stages:

    Vehicle Data
        ↓
    Preprocessing
        ↓
    Feature Engineering
        ↓
    Prediction
        ↓
    Recommendation
    """)

with col2:

    st.subheader("Microservices")

    st.write("""
    Independent services:

    • Data Service

    • Preprocessing Service

    • Prediction Service (ML)

    • Maintenance Service

    • Dashboard
    """)

# --------------------------------------------------
# Workflow
# --------------------------------------------------
st.header("🔄 Application Workflow")

st.markdown("""
1. Collect vehicle diagnostic data.
2. Preprocess the input data.
3. Train the Random Forest model.
4. Predict airbag maintenance status.
5. Generate maintenance recommendations.
6. Visualize results on the dashboard.
""")

# --------------------------------------------------
# Project Modules
# --------------------------------------------------
st.header("📂 Application Modules")

st.markdown("""
Use the **left sidebar** to navigate through the application.

- 🏠 Home
- 📥 Data Collection
- 🧹 Data Preprocessing
- 🤖 Model Training
- 🔍 Prediction
- 📊 Dashboard
""")

# --------------------------------------------------
# Input Features
# --------------------------------------------------
st.header("📋 Input Features")

st.table({
    "Feature":[
        "Vehicle Age",
        "Mileage",
        "Battery Voltage",
        "Temperature",
        "Humidity",
        "Warning Events",
        "Crash History",
        "Sensor Voltage",
        "ECU Health"
    ],
    "Description":[
        "Age of vehicle (Years)",
        "Distance travelled (km)",
        "Vehicle battery voltage",
        "Ambient temperature",
        "Operating humidity",
        "Airbag warning occurrences",
        "Previous crash count",
        "Airbag sensor voltage",
        "ECU health percentage"
    ]
})

# --------------------------------------------------
# Expected Output
# --------------------------------------------------
st.header("✅ Expected Output")

st.write("""
The application predicts:

- Airbag System Health
- Failure Probability
- Maintenance Recommendation
- Risk Level
""")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")

st.caption(
    "Software Engineering for Machine Learning | "
    "Predictive Maintenance for Automotive Airbag Systems"
)
