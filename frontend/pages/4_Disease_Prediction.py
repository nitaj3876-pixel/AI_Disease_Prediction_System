import streamlit as st
import requests
from pathlib import Path

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🩺",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

css = Path("style.css")

if css.exists():
    st.markdown(f"<style>{css.read_text()}</style>", unsafe_allow_html=True)

# ---------------- LOGIN CHECK ---------------- #

if "logged_in" not in st.session_state:
    st.warning("⚠ Please Login First")
    st.stop()

# ---------------- SIDEBAR ---------------- #

st.sidebar.image("assets/logo.png", width=120)

st.sidebar.title("🩺 MediPredict AI")

st.sidebar.success(f"👋 {st.session_state['user_name']}")

st.sidebar.markdown("---")

if st.sidebar.button("🏠 Dashboard"):
    st.switch_page("pages/4_Dashboard.py")

if st.sidebar.button("📜 History"):
    st.switch_page("pages/5_History.py")

if st.sidebar.button("📄 Report"):
    st.switch_page("pages/6_Report.py")

if st.sidebar.button("👤 Profile"):
    st.switch_page("pages/7_Profile.py")

if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.switch_page("pages/1_Login.py")

# ---------------- TITLE ---------------- #

st.title("🩺 AI Disease Prediction")

st.write("Select symptoms and click Predict Disease.")

st.divider()

# ---------------- SYMPTOMS ---------------- #

symptom_names = [

"fever",
"cough",
"fatigue",
"headache",
"vomiting",
"nausea",
"chest_pain",
"breathing_difficulty",
"joint_pain",
"skin_rash",
"itching",
"diarrhea",
"constipation",
"loss_of_appetite",
"weight_loss",
"weight_gain",
"back_pain",
"muscle_pain",
"sore_throat",
"runny_nose"

]

selected_vector = []

st.subheader("Select Symptoms")

cols = st.columns(2)

for i, symptom in enumerate(symptom_names):

    if cols[i % 2].checkbox(symptom.replace("_"," ").title()):

        selected_vector.append(1)

    else:

        selected_vector.append(0)

st.divider()

# ---------------- PREDICT ---------------- #

if st.button("🧠 Predict Disease", use_container_width=True):

    try:

        response = requests.post(

            "http://127.0.0.1:8000/predict",

            json={

               "email": st.session_state.user_email,

                "symptoms": selected_vector

}

        )

        if response.status_code != 200:

            st.error("Prediction Failed")

        else:

            result = response.json()

            st.success("Prediction Completed Successfully ✅")

            st.divider()

            c1,c2=st.columns(2)

            with c1:

                st.subheader("🦠 Disease")

                st.success(result["disease"])

                st.subheader("🎯 Confidence")

                st.progress(result["confidence"]/100)

                st.write(f"### {result['confidence']}%")

            with c2:

                st.subheader("👨‍⚕ Doctor")

                st.info(result["doctor"])

                st.subheader("🥗 Diet")

                st.info(result["diet"])

            st.divider()

            st.subheader("💊 Precautions")

            for item in result["precautions"]:

                st.write("✅",item)

            # Save Latest Prediction

            st.session_state["latest_prediction"]=result

    except Exception as e:

        st.error(f"Error : {e}")

st.divider()

st.markdown(
"""
<div style="text-align:center;color:gray;">

© 2026 MediPredict AI

</div>
""",
unsafe_allow_html=True
)