import streamlit as st

st.title("Salomlashuv ilovasi")

ism = st.text_input("Ismingizni kiriting")

if st.button("Salomlashish"):
    if ism.strip():
        st.success(f"Assalomu alaykum, {ism}!")
    else:
        st.warning("Avval ismingizni kiriting.")
