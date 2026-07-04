import streamlit as st
import pandas as pd

st.title("🧹 Data Preprocessing")

if "raw_data" not in st.session_state:
    st.warning("Please upload data first.")
    st.stop()

df = st.session_state["raw_data"].copy()

st.subheader("Raw Data")
st.dataframe(df)

# Handle missing values only
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

st.session_state["processed_data"] = df

st.subheader("Processed Data")
st.dataframe(df)

st.success("Data preprocessing completed.")
