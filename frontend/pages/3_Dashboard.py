import streamlit as st
from pathlib import Path

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- CSS ---------------- #

css = Path("style.css")

if css.exists():
    st.markdown(f"<style>{css.read_text()}</style>", unsafe_allow_html=True)

# ---------------- Login Check ---------------- #

if "logged_in" not in st.session_state:
    st.warning("⚠ Please Login First")
    st.stop()

# ---------------- Sidebar ---------------- #

st.sidebar.image("assets/logo.png", width=140)

st.sidebar.title("🩺 MediPredict AI")

st.sidebar.success("AI Healthcare")

st.sidebar.markdown("---")

st.sidebar.write("👤", st.session_state["user_name"])

if st.sidebar.button("🚪 Logout"):

    st.session_state.clear()

    st.switch_page("pages/1_Login.py")

# ---------------- Header ---------------- #

st.markdown(f"""
<h1 style='color:white;'>

Welcome,

<span style='color:#00E5C3;'>

{st.session_state["user_name"]}

</span>

👋

</h1>
""", unsafe_allow_html=True)

st.write("")

# ---------------- Statistics ---------------- #

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("🤒 Predictions","125","+12")

with c2:
    st.metric("📄 Reports","85","+8")

with c3:
    st.metric("👨‍⚕ Diseases","42","+2")

with c4:
    st.metric("🎯 Accuracy","95%","+1%")

st.write("")
st.divider()

# ---------------- Quick Actions ---------------- #

st.subheader("⚡ Quick Actions")

a,b,c=st.columns(3)

with a:

    if st.button("🤒 Predict Disease",use_container_width=True):
        st.switch_page("pages/4_Disease_Prediction.py")

with b:

    if st.button("📜 Prediction History",use_container_width=True):
        st.switch_page("pages/5_History.py")

with c:

    if st.button("📄 Download Report",use_container_width=True):
        st.success("Coming Soon")

st.write("")
st.divider()

# ---------------- Recent Predictions ---------------- #

st.subheader("📋 Recent Predictions")

data=[

["01/07/2026","Diabetes","92%"],

["03/07/2026","Malaria","89%"],

["06/07/2026","Heart Disease","95%"]

]

st.table(data)

st.write("")
st.divider()

# ---------------- Tips ---------------- #

st.subheader("💡 Health Tips")

st.info("""

🥗 Eat Healthy

💧 Drink More Water

🏃 Exercise Daily

😴 Sleep 8 Hours

""")

st.write("")

# ---------------- Footer ---------------- #

st.markdown("""

<div style='text-align:center;color:gray;'>

© 2026 MediPredict AI

FastAPI • Streamlit • Machine Learning

</div>

""",unsafe_allow_html=True)