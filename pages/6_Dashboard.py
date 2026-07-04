import streamlit as st
import matplotlib.pyplot as plt
st.title("📊 Dashboard")
if "prediction" in st.session_state:
 st.metric("Status",st.session_state["prediction"]["status"]); st.metric("Confidence",f"{st.session_state['prediction']['prob']:.2%}")
if "processed_data" in st.session_state:
 fig,ax=plt.subplots(); st.session_state["processed_data"].iloc[0].plot(kind="bar",ax=ax); st.pyplot(fig)
