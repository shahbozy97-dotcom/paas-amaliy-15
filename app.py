import streamlit as st

st.title("Xavfsiz bulutli kalkulyator")

a = st.number_input("Birinchi son", value=0.0)
b = st.number_input("Ikkinchi son", value=0.0)

amal = st.selectbox(
    "Amalni tanlang",
    ["Qo'shish", "Ayirish", "Ko'paytirish", "Bo'lish"]
)

if st.button("Hisoblash"):
    if amal == "Qo'shish":
        natija = a + b
    elif amal == "Ayirish":
        natija = a - b
    elif amal == "Ko'paytirish":
        natija = a * b
    else:
        if b == 0:
            st.warning("Nolga bo'lish mumkin emas!")
            st.stop()
        natija = a / b

    st.success(f"Natija: {natija:g}")
