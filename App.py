import streamlit as st

from PIL import Image

with st.form(key='My Form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('login')

img = Image.open("IEC group.Jpg")
st.sidebar.image(img.resize((200,200)))

st.checkbox("Agree")
st.title("My First WebApp")

st.subheader ("Using Python")

w=st.sidebar.number_input ("Your weight")
H=st.sidebar.number_input ("Your Height in meters")

def bmi_calc(w,h):
    BMI = round (w/(H**2),1)
    return BMI

if st.sidebar.button("Calculate"):
    st.balloons()
    st.sidebar.write (bmi_calc(w,H))

a1,a2 = st.columns (2)

with a1:
    st.number_input ("How old are you presently?", step=1)
    st.text_input ("What State are you from?")
    st.text_area ("Your present location?")
    st.checkbox("Accept")
    
with a2:
    st.date_input("Date of Last Visit")
    st.selectbox("Gender",["None","Male", "Female", "others"])
    st.text_area ("Why do you want to study Python?")
    st.checkbox("Reject")




               




