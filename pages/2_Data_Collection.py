import streamlit as st
import pandas as pd
st.title("📥 Data Collection")
u=st.file_uploader("Upload CSV",type="csv")
if u:
 df=pd.read_csv(u); st.session_state["raw_data"]=df; st.dataframe(df)
else:
 vals={"VehicleAge":st.number_input("Vehicle Age",0,30,5),"Mileage":st.number_input("Mileage",0,300000,50000),"BatteryVoltage":st.number_input("Battery Voltage",10.0,15.0,12.5),"Temperature":st.number_input("Temperature",-20,60,30),"Humidity":st.number_input("Humidity",0,100,50),"WarningEvents":st.number_input("Warning Events",0,20,0),"CrashHistory":st.number_input("Crash History",0,10,0),"SensorVoltage":st.number_input("Sensor Voltage",0.0,5.0,4.8),"ECUHealth":st.number_input("ECU Health",0,100,95)}
 if st.button("Save"): st.session_state["raw_data"]=pd.DataFrame([vals]); st.success("Saved")
