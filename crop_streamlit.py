import predict
from google.cloud import aiplatform
import numpy as np
import streamlit as st

st.set_page_config(layout='centered')
st.header("What Crop is Best for Your Soil?")

N = st.number_input("Nitrogen", 1,150)
P = st.number_input("Phosporus", 1,150)
K = st.number_input("Potassium", 1,225)
temp = st.number_input("Temperature in Celcius",0.0,50.0)
humidity = st.number_input("Humidity in %", 0.0,100.0)
ph = st.number_input("Soil pH", 0.0,14.0)
rainfall = st.number_input("Rainfall in mm",0.0,300.0)

model_input = [N,P,K,temp,humidity,ph,rainfall]

crop_list = ['Watermelon','Rice','Pomegranate','Pigeon Peas','Papaya','Orange','Muskmelon','Mung Beans','Moth Beans','Mango','Maize','Lentil','Kidney Beans','Jute','Grapes','Cotton','Coffee','Coconut','Chickpea','Blackgram','Banana','Apple']

if st.button('Predict'):
    probs = predict.predict_custom_trained_model_sample(
        project="554698915331",
        endpoint_id="6625397584234020864",
        location="us-central1",
        instances=[model_input]
    )
#print(probs)
    st.write(f"The best crop for you is {crop_list[np.argmax(probs)]}")