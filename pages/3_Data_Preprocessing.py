import streamlit as st
from sklearn.preprocessing import StandardScaler
st.title("🧹 Data Preprocessing")
if "raw_data" not in st.session_state: st.stop()
df=st.session_state["raw_data"].copy(); st.dataframe(df)
df=df.fillna(df.mean(numeric_only=True)); scaler=StandardScaler(); df[df.columns]=scaler.fit_transform(df); st.session_state["processed_data"]=df; st.dataframe(df)
