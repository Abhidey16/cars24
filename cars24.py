import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title("Car Price Prediction App")


col1, col2,col3 = st.columns(3)

with col1: 

    fuel_type = st.radio("Fuel Type", ["Petrol", "Diesel", "Electric","LPG"])

with col2: 
    Vehical_type = st.selectbox("Vehical Type", ["Manual", "Automatic"])

# with col3:
#     age = st.selectbox("age of car",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])


col4, col5, col6 = st.columns(3)

with col4:
    engine_power = st.slider("Engine Power (CC)", 500, 5000, step=100)

with col5:
    seat = st.selectbox("Seats", [2, 4, 5, 6, 7, 8, 9, 10])
    
with col6:
    mileage = st.slider("mileage", 5, 120, step=2)
    

col7, col8, col9 = st.columns(3)

with col7:
    km_driven = st.slider("KM Driven", 1000, 100000, step=1000)

with col8:
    max_power= st.slider("max speed (HP)", 60, 500, step=20)

# with col9:
#     make = st.selectbox("Company", ['MARUTI', 'HYUNDAI'])
    
col11, col12, col13 = st.columns(3)
with col11:
    year = st.slider("year",2010, 2023, step=1)

with col12:
    seller_type = st.selectbox("Seller type", ["Individual", "Dealer"])
  
# with col13:
#     age = st.slider("Age of Car",1, 20, step=1)
  
    
    
model = pickle.load(open("car_pred", "rb"))

encode_dict={
    "fuel_type": {"Diesel": 1, "Petrol": 2, "LPG": 3, "Electric": 4},
    "Vehical": {"Manual": 1, "Automatic": 2},
    "Company": {"MARUTI":1, 'HYUNDAI':2},
    "Seller_type" : {"Individual":1,"Dealer":2}
     }



def model_pred(year,seller_type,km_driven,fuel_type,Vehical_type,mileage,engine_power,max_power,seat):

    Vehical_type = encode_dict["Vehical"][Vehical_type]
    fuel_type = encode_dict["fuel_type"][fuel_type]
    # make = encode_dict["Company"][make]
    seller_type = encode_dict["Seller_type"][seller_type]

    data = [[year,seller_type,km_driven,fuel_type,Vehical_type,mileage,engine_power,max_power,seat]]
 
    return np.round(model.predict(data)[0],2)


if st.button("Predict"):
    st.write(model_pred(year,seller_type,km_driven,fuel_type,Vehical_type,mileage,engine_power,max_power,seat))
else:
    st.write("Click on Predict, once you're done with the data")


    