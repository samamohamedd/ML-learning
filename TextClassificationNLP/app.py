import streamlit as st
import helper
import pickle
import sklearn

model = pickle.load(open("models/model.pkl", 'rb'))
vectorizer = pickle.load(open("models/vectorizer.pkl", 'rb'))

st.title("Sentiment Analysis using ML")

text = st.text_input("Please enter your review")

state = st.button("predict")

token = helper.preprocessing_step(text)
vectorized_data = vectorizer.transform([token])
prediction = model.predict(vectorized_data)

if prediction[0] == 0: prediction = "Negative"
if prediction[0] == 1: prediction = "Positive"

if state :
    st.text(prediction)