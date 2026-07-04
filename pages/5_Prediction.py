import streamlit as st,joblib
st.title("🔍 Prediction")
if "processed_data" not in st.session_state: st.stop()
model=joblib.load("model.pkl")
if st.button("Predict"):
 p=model.predict(st.session_state["processed_data"])[0]; pr=model.predict_proba(st.session_state["processed_data"])[0].max(); st.session_state["prediction"]={"status":"Maintenance Required" if p==1 else "Healthy","prob":pr}; st.write(st.session_state["prediction"])
