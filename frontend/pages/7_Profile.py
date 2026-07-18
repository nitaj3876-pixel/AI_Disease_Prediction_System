import streamlit as st
import requests
from pathlib import Path

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

css = Path("style.css")

if css.exists():
    st.markdown(
        f"<style>{css.read_text()}</style>",
        unsafe_allow_html=True
    )

# ---------------- LOGIN CHECK ---------------- #

if "logged_in" not in st.session_state:
    st.warning("⚠ Please Login First")
    st.stop()

# ---------------- SIDEBAR ---------------- #

st.sidebar.image("assets/logo.png", width=120)

st.sidebar.title("🩺 MediPredict AI")

st.sidebar.success(f"👋 {st.session_state.user_name}")

st.sidebar.markdown("---")

if st.sidebar.button("🏠 Dashboard"):
    st.switch_page("pages/3_Dashboard.py")

if st.sidebar.button("🤒 Disease Prediction"):
    st.switch_page("pages/4_Disease_Prediction.py")

if st.sidebar.button("📜 History"):
    st.switch_page("pages/5_History.py")

if st.sidebar.button("📄 Report"):
    st.switch_page("pages/6_Report.py")

if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.switch_page("pages/1_Login.py")

# ---------------- TITLE ---------------- #

st.title("👤 My Profile")

st.write("View and update your profile information.")

st.divider()

# ---------------- LOAD PROFILE ---------------- #

try:

    response = requests.get(
        f"https://ai-disease-prediction-system-znq7.onrender.com/profile/{st.session_state.user_email}"
    )

    profile = response.json()

except:

    profile = {}

if profile == {}:

    st.error("Profile Not Found")

    st.stop()

# ---------------- FORM ---------------- #

with st.form("profile_form"):

    name = st.text_input(
        "Full Name",
        value=profile["name"]
    )

    email = st.text_input(
        "Email",
        value=profile["email"],
        disabled=True
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=int(profile["age"])
    )

    gender = st.selectbox(

        "Gender",

        ["Male","Female","Other"],

        index=["Male","Female","Other"].index(profile["gender"])

    )

    submit = st.form_submit_button(
        "💾 Update Profile"
    )

if submit:

    data = {

        "name": name,

        "email": email,

        "password": "dummy",

        "age": age,

        "gender": gender

    }

    response = requests.put(

        f"https://ai-disease-prediction-system-znq7.onrender.com/profile/{email}",

        json=data

    )

    result = response.json()

    st.success(result["message"])

    st.session_state.user_name = name

st.divider()

# ---------------- USER CARD ---------------- #

st.subheader("📋 Account Information")

c1,c2 = st.columns(2)

with c1:

    st.metric("👤 Name", profile["name"])

    st.metric("🎂 Age", profile["age"])

with c2:

    st.metric("📧 Email", profile["email"])

    st.metric("⚧ Gender", profile["gender"])

st.divider()

st.markdown("""

<div style="text-align:center;color:gray">

© 2026 MediPredict AI

FastAPI • Streamlit • Machine Learning

</div>

""", unsafe_allow_html=True)