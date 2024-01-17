import requests
import streamlit as st
from PIL import Image
import joblib
Ypredict=0
animation = Image.open("usedcar.gif")
st.set_page_config(page_title="Used cars prediction", page_icon=":car:", layout="wide")
with st.container():
    left_column, right_column = st.columns((2, 1))
    with left_column:
            st.title("Used car price prediction")
            st.subheader("This web page is for car prediction price")
            st.write("To predict your car's price , you must provide all the data we need.")
    with right_column:
            st.image(animation)
with st.container():
    st.write("---")
    left_column,middle_column, right_column = st.columns(3)
    with left_column:
        fuel = st.radio(":red[Fuel type] :fuelpump:",["Petrol", "Diesel", "GNC"],index=None)

        if fuel == 'Petrol':
            Diesel=0
            Petrol=1
            CNG=0
        elif fuel == 'Diesel':
            Diesel=1
            Petrol=0
            CNG=0
        else:
            Diesel=0
            Petrol=0
            CNG=1
    with right_column:
        Transmission = st.radio(":grey[Transmission] :gear:",["Automatic", "Manual"])
        if Transmission == 'Automatic':
            Auto=1
            Man=0
        else:
            Auto=0
            Man=1

with st.container():
    st.write("---")
    left_column,middle_column, right_column = st.columns(3)
    with left_column:
        manufacturing_year = st.number_input('Manufacturing year',placeholder="Type a number...")
    with middle_column:
        kms_driven = st.number_input('Kilometers driven',placeholder="Type a number...")
    with right_column:
        mileage = st.number_input('Milage',placeholder="Type a number...")

with st.container():
    st.write("---")
    left_column,middle_column, right_column = st.columns(3)
    with left_column:
        engine = st.number_input('engine',placeholder="Type a number...")
    with middle_column:
        torque = st.number_input('Torque',placeholder="Type a number...")
    with right_column:
        st.button("Calculate", type="primary")
        if st.button("Calculate"):
            filename = "Usedcars_model.joblib"
            loaded_model = joblib.load(filename)
            Ypredict = loaded_model.predict([[Petrol, Diesel,Man,Auto,mileage,manufacturing_year,kms_driven,CNG,torque,
            engine]])
with st.container():
    st.write(":moneybag: Your car price is :")
    st.write(Ypredict)
