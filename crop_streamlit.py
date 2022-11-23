import predict
from google.cloud import aiplatform
import google.auth
import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

creds,proj_id = google.auth.default()
aiplatform.init(credentials=creds,project=proj_id)

st.set_page_config(layout='centered')
st.title("What Crop Should You Plant?")
st.write("This model will recommend the most suitable crop to plant based on soil and environmental factors.  This can provide information valuable to setting a farming strategy for optimizing yields. The model is trained on Indian agriculture data.")


col1,col2  = st.columns([2,2])

with col1:
    N = st.number_input("Nitrogen", 1,150)
    P = st.number_input("Phosporus", 1,150)
    K = st.number_input("Potassium", 1,225)
    temp = st.number_input("Temperature in Celcius",0.0,50.0)


with col2:
    humidity = st.number_input("Humidity in %", 0.0,100.0)
    ph = st.number_input("Soil pH", 0.0,14.0)
    rainfall = st.number_input("Rainfall in mm",0.0,300.0)

model_input = [N,P,K,temp,humidity,ph,rainfall]

crop_list = ['Watermelon','Rice','Pomegranate','Pigeon Peas','Papaya','Orange','Muskmelon','Mung Beans','Moth Beans','Mango','Maize','Lentil','Kidney Beans','Jute','Grapes','Cotton','Coffee','Coconut','Chickpea','Blackgram','Banana','Apple']

if st.button('Predict'):
    probs = predict.predict_custom_trained_model_sample(
        project="717860154136",
        endpoint_id="3838513839821815808",
        # project="554698915331",
        # endpoint_id="6625397584234020864",
        location="us-central1",
        instances=[model_input]
    )
    crop=crop_list[np.argmax(probs)]
    html_str = f"""
    <style>
    p.a {{
    font-size: 36px;
    text-align: center;
    }}
    .output {{
        color: #ff0000;
    }}
    </style>
    <p class='a'>The best crop for you is <span class='output'>{crop}</span></p>
    """
    st.markdown(html_str, unsafe_allow_html=True,)
    
    fig, ax = plt.subplots()
    ax.bar(x=crop_list,height=probs)
    ax.tick_params(labelrotation=90)    
    ax.set_xlabel("Crop")
    ax.set_ylabel("Recommendation Confidence")
    st.pyplot(fig)