import streamlit as st,pandas as pd,joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
st.title("🤖 Model Training")
path=st.text_input("Dataset","airbag_dataset.csv")
if st.button("Train"):
 d=pd.read_csv(path); X=d.drop("MaintenanceRequired",axis=1); y=d["MaintenanceRequired"]; Xtr,Xte,Ytr,Yte=train_test_split(X,y,test_size=0.2,random_state=42); m=RandomForestClassifier(random_state=42); m.fit(Xtr,Ytr); acc=accuracy_score(Yte,m.predict(Xte)); joblib.dump(m,"model.pkl"); st.metric("Accuracy",f"{acc:.2%}")
