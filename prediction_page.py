import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pk1', 'rb') as file:
        data = pickle.load(file)
        return data
data=load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_prediction_page():
    st.title('SOFTWARE DEVELOPER SALARY PREDICTION 2023')

    st.write("""### WE NEED SOME INFORMATION TO PREDICT YOUR SALARY""")

    countries=(
        'United States of America',
        'Germany',
        'United Kingdom of Great Britain and Northern Ireland',   
        'India',                                                 
        'Canada',                                               
        'France',                                                  
        'Poland',                                                   
        'Brazil',                                                  
        'Netherlands',                                             
        'Australia',                                               
        'Spain',                                                   
        'Italy',                                                  
        'Sweden', 
    )
    education=(
        'Bachelor’s degree (B.A., B.S., B.Eng., etc.)',                                        
        'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)',
        'University study without earning a degree',                                 
        'Professional degree (JD, MD, Ph.D, Ed.D, etc.)',                                        
        'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)',      
        'Associate degree (A.A., A.S., etc.)',                                                     
        'Something else',
        'Primary/elementary school',
    )
    country=st.selectbox('COUNTRY',countries)
    education=st.selectbox('EDUCATION LEVEL',education)
    YearsCode=st.slider('YEARS OF CODING',0,50,3)
    WorkExp=st.slider('YEARS OF WORKING EXPERIENCE',0,50,3)

    ok=st.button('CALCULATE SALARY')
    if ok:
        X=np.array([[country,education,YearsCode,WorkExp]])
        X[:,0]=le_country.transform(X[:,0])
        X[:,1]=le_education.transform(X[:,1])
        X=X.astype(float)

        Salary=regressor.predict(X)
        st.subheader(f"The estimated salary is ${Salary[0]:.2f}")
show_prediction_page()

