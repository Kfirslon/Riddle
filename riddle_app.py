import streamlit as st
import random
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Riddle",
    page_icon="🎭",
    layout="centered"
)

# Custom CSS for modern, clean look and minimal spacing
st.markdown("""
    <style>
    html, body, .stApp {
        font-family: 'Segoe UI', Arial, Helvetica, sans-serif !important;
        background-color: #1a1a1a;
        color: #ffccdd;
    }
    .custom-title {
        text-align: center;
        color: #ffc0cb;
        font-size: 2.5em;
        font-weight: 700;
        margin-bottom: 0;
        letter-spacing: 1px;
        line-height: 1.1;
    }
    .custom-hr {
        border: none;
        border-top: 5px solid #ffc0cb !important; /* THIS IS THE LINE BELOW RIDDLE - made thicker and more visible */
        margin: -0.5em 0 0 0;
        width: 100%;
        background: none;
    }
    .main .block-container {
        padding-top: 0.1rem !important;
    }
    /* THIS IS THE FORM BORDER/FRAMEWORK - Streamlit's default form container */
    .stForm {
        border: 3px solid #ffc0cb !important; /* Added visible pink border around form */
        border-radius: 15px !important; /* Rounded corners */
        padding: 20px !important; /* Add some padding inside the form */
        background-color: rgba(255, 192, 203, 0.1) !important; /* Light pink background */
        margin: 20px 0 !important; /* Add some margin around the form */
    }
    .stTextInput>div>div {
        max-width: none;
        margin: 0;
    }
    .stTextInput>div>div>input {
        background-color: transparent !important;
        color: #1a1a1a;
        font-size: 1.1em;
        border-radius: 8px;
        border: 2px solid #ddd;
        transition: background 0.2s, border 0.2s;
        font-family: 'Segoe UI', Arial, Helvetica, sans-serif !important;
    }
    .stTextInput>div>div>input:focus {
        background-color: #e0f0ff !important;
        border: 2px solid #3399ff !important;
    }
    label, .css-1cpxqw2, .css-1n76uvr, .css-1y4p8pa, .css-1q8dd3e {
        color: #ffc0cb !important;
        font-weight: 600 !important;
        font-size: 1.1em !important;
        font-family: 'Segoe UI', Arial, Helvetica, sans-serif !important;
        margin-bottom: 0.2em !important;
    }
    .stButton>button {
        background-color: #d72660 !important;
        color: #fff !important;
        border: none;
        padding: 18px 0;
        border-radius: 12px;
        width: 60% !important;
        max-width: 400px;
        margin: 1.5em auto 0 auto;
        display: block;
        font-size: 1.4em;
        font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
        font-weight: 900;
        box-shadow: 0 2px 12px #00000022;
        transition: background 0.2s;
        letter-spacing: 1px;
    }
    /* ANSWER BUTTON STYLING - This targets the form submit button specifically */
    .stForm .stButton>button {
        background-color: #ffc0cb !important; /* Pink background like your image */
        color: #ffffff !important; /* White text */
        border: 2px solid #ffffff !important; /* White border */
        font-weight: 700 !important;
        box-shadow: 0 4px 15px rgba(255, 192, 203, 0.4) !important; /* Pink glow */
        width: 100% !important; /* NEW - full width like in image */
        margin: 1em auto 0 auto !important; /* NEW - center it */
    }
    .stForm .stButton>button:hover {
        background-color: #a51c4b !important; /* Darker pink on hover */
        color: #ffffff !important;
        border: 2px solid #ffffff !important;
    }
    .stButton>button:hover {
        background-color: #a51c4b !important;
        color: #fff !important;
    }
    .success-message {
        color: #32cd32;
        font-size: 1.3em;
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
        font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'show_buttons' not in st.session_state:
    st.session_state.show_buttons = False
if 'show_success' not in st.session_state:
    st.session_state.show_success = False
if 'stored_day' not in st.session_state:
    st.session_state.stored_day = ""
if 'stored_name' not in st.session_state:
    st.session_state.stored_name = ""

# Dynamic title
if st.session_state.show_buttons or st.session_state.show_success:
    title = f"Riddle for {st.session_state.stored_name or '...'}"
else:
    title = "Riddle"

st.markdown(f"<div class='custom-title'>{title}</div>", unsafe_allow_html=True)
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)

# Full-width form
with st.form("riddle_form"):
    name = st.text_input("Your Name:")
    location = st.text_input("Current City:")
    food = st.text_input("Food:")
    day = st.text_input("Day:")
    color = st.text_input("Color:")
    submitted = st.form_submit_button("Answer")

# Handle form submission
if submitted:
    st.session_state.stored_day = day
    st.session_state.stored_name = name
    st.session_state.show_buttons = True
    st.session_state.show_success = False

    # Display the riddle
    riddle_text = f"""
    Hope you're ready {name or 'friend'},<br>because,<br>We were in {location},<br>And, your {food} was right.<br>Go out with me {day} night? 🌹
    """

    st.markdown(
        f'<div style="background-color: #2c2c2c; border: 3px solid #ffc0cb; padding: 25px; border-radius: 15px; color: #ffffff; font-size: 1.3em; text-align: center; margin-bottom: 1.5em; font-family: Segoe UI, Arial, Helvetica, sans-serif; font-weight: 600;">{riddle_text}</div>',
        unsafe_allow_html=True
    )

# Show buttons if form was submitted
if st.session_state.show_buttons:
    col1, col2 = st.columns(2)
    yes_clicked = col1.button("Yes 💚")

    # Custom HTML/JS for "No" button that moves away from the mouse
    no_btn_html = '''
    <div id="no-btn-container" style="position:relative; height:80px; width:180px;">
      <button id="no-btn" style="position:absolute; left:40px; top:20px; background-color:#ff4444; color:white; border:none; border-radius:8px; padding:10px 25px; font-size:18px; cursor:pointer; font-family: 'Segoe UI', Arial, Helvetica, sans-serif; font-weight: 700;">
        No ❌
      </button>
    </div>
    <script>
    const btn = document.getElementById('no-btn');
    const container = document.getElementById('no-btn-container');
    function moveBtn(e) {
      const rect = btn.getBoundingClientRect();
      const mouseX = e.clientX;
      const mouseY = e.clientY;
      const btnX = rect.left + rect.width/2;
      const btnY = rect.top + rect.height/2;
      const dist = Math.sqrt((mouseX - btnX)**2 + (mouseY - btnY)**2);
      if (dist < 80) {
        const maxX = container.offsetWidth - btn.offsetWidth;
        const maxY = container.offsetHeight - btn.offsetHeight;
        const x = Math.floor(Math.random() * (maxX > 0 ? maxX : 1));
        const y = Math.floor(Math.random() * (maxY > 0 ? maxY : 1));
        btn.style.left = x + 'px';
        btn.style.top = y + 'px';
      }
    }
    container.onmousemove = moveBtn;
    btn.onclick = function(e) { e.preventDefault(); };
    </script>
    '''
    col2.markdown(no_btn_html, unsafe_allow_html=True)

    if yes_clicked:
        st.session_state.show_buttons = False
        st.session_state.show_success = True
        st.balloons()

# Show success message
if st.session_state.show_success:
    st.markdown(
        f'<div class="success-message">{st.session_state.stored_day} night confirmed. Use your WhatsApp for more details 🎉</div>',
        unsafe_allow_html=True
    )