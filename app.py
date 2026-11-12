
import streamlit as st

st.set_page_config(page_title="Talaba PaaS ilovasi")

st.title("Talabaning bulutli ilovasi")
st.header("Bulutli texnologiyalar")
st.info("GitHub va Streamlit asosidagi loyiha")

st.subheader("Talaba ma'lumotlari")

ism = st.text_input("Ismingizni kiriting")
guruh = st.text_input("Guruhingizni kiriting")

if st.button("Talaba ma'lumotlari"):
    if ism.strip() and guruh.strip():
        st.success(f"Salom, {ism}!")
        st.write(f"Guruhingiz: {guruh}")
    else:
        st.warning("Barcha maydonlarni to'ldiring.")

st.divider()

st.subheader("Bulutli kalkulyator")

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

st.divider()
st.caption("Bulutli texnologiyalar amaliy mashg'uloti")
