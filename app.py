
import streamlit as st

st.set_page_config(page_title="Talabaning shaxsiy bulutli kalkulyatori")

st.title("Talabaning shaxsiy bulutli kalkulyatori")
st.header("Bulutli texnologiyalar fani")
st.subheader("Amaliy mashg'ulot")

st.write("GitHub va Streamlit platformalari")

st.info("Bu ilova bulutda ishlamoqda.")
st.success("Dastur muvaffaqiyatli ishga tushdi!")
st.warning("Ma'lumotlarni tekshirib kiriting.")

st.divider()

st.subheader("Xavfsiz bulutli kalkulyator")

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
            st.error("Nolga bo'lish mumkin emas!")
            st.stop()
        natija = a / b

    st.success(f"Natija: {natija:g}")

st.caption("Bulutli texnologiyalar amaliy mashg'uloti")
