import streamlit as st
import requests

st.set_page_config(
    page_title="Patient Login",
    page_icon="🔐",
    layout="centered"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🔐 Patient Login")

email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")

if st.button("Login", use_container_width=True):

    data = {
        "email": email,
        "password": password
    }

    try:
        response = requests.post(
            "https://ai-disease-prediction-system-znq7.onrender.com",
            json=data
        )

        # Server Error Check
        if response.status_code != 200:
            st.error(response.text)
            st.stop()

        # JSON Response
        result = response.json()
        st.write(result)

        if result["message"] == "Login Successful":

            st.session_state["logged_in"] = True
            st.session_state["user_name"] = result["name"]
            st.session_state["user_email"] = result["email"]
            st.session_state["token"] = result["token"]

            st.success("✅ Login Successful")

            st.switch_page("pages/3_Dashboard.py")

        else:
            st.error(result["message"])

    except Exception as e:
        st.error(f"Error : {e}")

st.divider()

if st.button("📝 Create New Account"):
    st.switch_page("pages/2_Register.py")