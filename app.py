import streamlit as st

st.title("Bulutli kalkulyator")

a = st.number_input("Birinchi son", value=0)
b = st.number_input("Ikkinchi son", value=0)

if st.button("Hisoblash"):
    st.write("Yig'indi:", a + b)
    st.write("Ayirma:", a - b)
    st.write("Ko'paytma:", a * b)
