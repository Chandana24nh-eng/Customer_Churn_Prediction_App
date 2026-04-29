import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open("model.pkl","rb"))

st.title("Customer Churn Prediction")

gender = st.selectbox("Gender",["Male","Female"])
senior = st.selectbox("Senior Citizen",["Yes","No"])
partner = st.selectbox("Partner",["Yes","No"])
dependents = st.selectbox("Dependents",["Yes","No"])

tenure = st.number_input("Tenure",0,72,12)

phone = st.selectbox("Phone Service",["Yes","No"])
multiple = st.selectbox("Multiple Lines",["Yes","No"])

online_security = st.selectbox("Online Security",["Yes","No"])
online_backup = st.selectbox("Online Backup",["Yes","No"])
device_protection = st.selectbox("Device Protection",["Yes","No"])
tech_support = st.selectbox("Tech Support",["Yes","No"])

tv = st.selectbox("Streaming TV",["Yes","No"])
movies = st.selectbox("Streaming Movies",["Yes","No"])

paperless = st.selectbox("Paperless Billing",["Yes","No"])

monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

internet = st.selectbox(
"Internet Service",
["DSL","Fiber optic","No"]
)

contract = st.selectbox(
"Contract",
["Month-to-month","One year","Two year"]
)

payment = st.selectbox(
"Payment Method",
[
"Bank transfer (automatic)",
"Credit card (automatic)",
"Electronic check",
"Mailed check"
]
)

# Encoding
data = pd.DataFrame({

'gender':[1 if gender=="Male" else 0],
'SeniorCitizen':[1 if senior=="Yes" else 0],
'Partner':[1 if partner=="Yes" else 0],
'Dependents':[1 if dependents=="Yes" else 0],
'tenure':[tenure],
'PhoneService':[1 if phone=="Yes" else 0],
'MultipleLines':[1 if multiple=="Yes" else 0],
'OnlineSecurity':[1 if online_security=="Yes" else 0],
'OnlineBackup':[1 if online_backup=="Yes" else 0],
'DeviceProtection':[1 if device_protection=="Yes" else 0],
'TechSupport':[1 if tech_support=="Yes" else 0],
'StreamingTV':[1 if tv=="Yes" else 0],
'StreamingMovies':[1 if movies=="Yes" else 0],
'PaperlessBilling':[1 if paperless=="Yes" else 0],
'MonthlyCharges':[monthly],
'Total_charges':[total],

'InternetService_DSL':[1 if internet=="DSL" else 0],
'InternetService_Fiber optic':[1 if internet=="Fiber optic" else 0],
'InternetService_No':[1 if internet=="No" else 0],

'Contract_Month-to-month':[1 if contract=="Month-to-month" else 0],
'Contract_One year':[1 if contract=="One year" else 0],
'Contract_Two year':[1 if contract=="Two year" else 0],

'PaymentMethod_Bank transfer (automatic)':
[1 if payment=="Bank transfer (automatic)" else 0],

'PaymentMethod_Credit card (automatic)':
[1 if payment=="Credit card (automatic)" else 0],

'PaymentMethod_Electronic check':
[1 if payment=="Electronic check" else 0],

'PaymentMethod_Mailed check':
[1 if payment=="Mailed check" else 0]

})

if st.button("Predict"):
    pred = model.predict(data)

    if pred[0]==1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")