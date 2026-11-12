import streamlit as st

st.title("Talaba ma'lumotlari")

ism = st.text_input("Ismingizni kiriting")
guruh = st.text_input("Guruhingizni kiriting")
fan = st.text_input("Fan nomini kiriting")

st.subheader("Kiritilgan ma'lumotlar")

st.write("Talaba ismi:", ism)
st.write("Guruh:", guruh)
st.write("Fan:", fan)
