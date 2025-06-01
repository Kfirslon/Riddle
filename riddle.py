import streamlit as st
import random

st.set_page_config(page_title="Riddle", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #ffc0cb;'>Riddle</h1><hr style='border-color: #ff99aa;'>",
    unsafe_allow_html=True
)

with st.form("riddle_form"):
    name = st.text_input("Your Name")
    location = st.text_input("Current City")
    food = st.text_input("Food")
    day = st.text_input("Day")
    color = st.text_input("Color")
    submitted = st.form_submit_button("Answer")

if submitted:
    st.markdown(
        f"<div style='background-color: {color or '#ffe6f0'}; padding: 25px; border-radius: 15px;'>"
        f"<p style='color: #1a1a1a; font-size: 20px;'>"
        f"Hope you're ready {name or 'friend'},<br>because,<br>"
        f"We were in {location},<br>"
        f"And, your {food} was right.<br>"
        f"Go out with me {day} night? 🌹"
        f"</p></div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    yes_clicked = col1.button("Yes 💚")
    no_clicked = col2.button("No ❌")

    if yes_clicked:
        st.success(f"{day} night confirmed. Use your WhatsApp for more details 🎉")
        st.balloons()

    if no_clicked:
        st.warning("Aww... maybe another time 😢")
