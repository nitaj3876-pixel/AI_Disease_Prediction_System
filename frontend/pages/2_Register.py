import streamlit as st
import requests
from pathlib import Path

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Register | MediPredict AI",
    page_icon="📝",
    layout="centered"
)

# ---------------- LOAD CSS ---------------- #

css = Path("style.css")

if css.exists():
    st.markdown(f"<style>{css.read_text()}</style>", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div style="text-align:center;">

<h1 style="color:white;">
🩺 MediPredict <span style="color:#00E5C3;">AI</span>
</h1>

<h2>Create Your Account</h2>

<p style="color:#cfcfcf;">
Join our AI Healthcare Platform
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- REGISTER FORM ---------------- #

with st.container():

    name = st.text_input("👤 Full Name")

    email = st.text_input("📧 Email")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    confirm_password = st.text_input(
        "🔒 Confirm Password",
        type="password"
    )

    age = st.number_input(
        "🎂 Age",
        min_value=1,
        max_value=120,
        value=20
    )

    gender = st.selectbox(
        "⚧ Gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )

st.write("")

# ---------------- REGISTER BUTTON ---------------- #

if st.button("📝 Create Account", use_container_width=True):

    if password != confirm_password:

        st.error("❌ Passwords do not match.")

    else:

        data = {

            "name": name,

            "email": email,

            "password": password,

            "age": age,

            "gender": gender

        }

        try:

            response = requests.post(
                "http://127.0.0.1:8000/register",
                json=data
            )

            result = response.json()

            if result["message"] == "User Registered Successfully":

                st.success("✅ Account Created Successfully!")

                st.balloons()

                st.switch_page("pages/1_Login.py")

            else:

                st.error(result["message"])

        except Exception as e:
           st.error(f"Error: {e}")

st.write("")

st.markdown("---")

col1, col2, col3 = st.columns([1,2,1])

with col2:

    if st.button(
        "🔐 Already have an account? Login",
        use_container_width=True
    ):
        st.switch_page("pages/1_Login.py")

st.write("")

st.markdown(
"""
<div style="text-align:center;color:gray;">
© 2026 MediPredict AI
</div>
""",
unsafe_allow_html=True
)