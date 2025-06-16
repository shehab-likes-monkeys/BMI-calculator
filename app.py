# import streamlit
import streamlit as st

# App Title
st.title('BMI Calculator')

# Taking user input
weight = st.number_input('Enter your weight (kg):', 10, 200)
height = st.number_input('Enter your height (cm):',100, 210)

# If button clicked
if st.button('Get your BMI'):
    height_m = height / 100
    bmi = weight / height_m ** 2
    st.write(f'Your BMI is: {bmi:.2f}')
