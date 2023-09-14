import streamlit as st
from exploratory_page import show_exploration_page
from prediction_page import show_prediction_page

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page=="Predict":
    show_prediction_page()
else:
    show_exploration_page()