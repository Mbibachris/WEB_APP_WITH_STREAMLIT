import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df=pd.read_csv('cleaned_developers_data')
    return df
df=load_data()

def show_exploration_page():
    st.title('EXPLORE SOFTWARE DEVELOPER SALARIES')
    st.write("""
    
    ### STACKOVERFLOW SURVEY 2023
    
    """)


    st.write("""#### NUMBER OF DATA FROM DIFFERENT COUNTRIES""")
    data=df['Country'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1) 


    st.write("""
    #### MEAN SALARY BASED ON COUNTRY
    
    """)
    data=df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)


    st.write("""
    #### MEAN SALARY BASED ON WORK EXPERIENCE
    """)
    data=df.groupby(['WorkExp'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)


    st.write(""" #### MEAN SALARY BASED EDUCATION LEVEL
    """)
    data=df.groupby(['Education'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(""" 
    #### MEAN SALARY BASED ON YEARS OF CODE
    """)
    data=df.groupby(['YearsCode'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)



