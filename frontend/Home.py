import streamlit as st
from pathlib import Path

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="MediPredict AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Load CSS
# ----------------------------
css_path = Path("style.css")

if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.image("assets/logo.png", width=140)

st.sidebar.title("🩺 MediPredict AI")

st.sidebar.markdown("---")

st.sidebar.success("AI Healthcare System")

# ----------------------------
# Top Navbar
# ----------------------------

col1, col2, col3 = st.columns([6,1,1])

with col1:
    st.markdown(
        """
        <h1 style="color:white;">
        🩺 MediPredict <span style="color:#00E5C3;">AI</span>
        </h1>
        """,
        unsafe_allow_html=True,
    )
col1, col2 = st.columns(2)
with col1:
 if st.button("🔐 Login"):
    st.switch_page("pages/1_Login.py")
with col2:
 if st.button("📝 Register"):
    st.switch_page("pages/2_Register.py")
st.write("")

# ----------------------------
# Hero Section
# ----------------------------

left, right = st.columns([1.2,1])

with left:

    st.markdown(
        """
        <h1 style="font-size:65px;color:white;line-height:1.1;">
        AI Powered<br>

        <span style="color:#16e0c9;">
        Disease Prediction
        </span>

        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    st.markdown(
        """
<div style='font-size:22px;color:#D8D8D8;'>

Predict diseases instantly using
Artificial Intelligence.

✔ Accurate Predictions

✔ Smart Healthcare

✔ Medical Reports

✔ AI Recommendations

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        st.button("🚀 Predict Now", use_container_width=True)

    with c2:
        st.button("📖 Learn More", use_container_width=True)

with right:

    st.image(
        "assets/doctor.png",
        use_container_width=True
    )

st.write("")
st.write("")

# ----------------------------
# Stats
# ----------------------------

st.subheader("📊 System Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Predictions",
        "10K+",
        "+250"
    )

with c2:
    st.metric(
        "Users",
        "5,000+",
        "+120"
    )

with c3:
    st.metric(
        "Diseases",
        "100+",
        "+5"
    )

with c4:
    st.metric(
        "Accuracy",
        "95%",
        "+2%"
    )

st.write("")
st.divider()

# ----------------------------
# Features
# ----------------------------

st.markdown(
    """
<h2 style="text-align:center;color:white;">
Why Choose MediPredict AI?
</h2>
""",
    unsafe_allow_html=True,
)

f1, f2, f3 = st.columns(3)

with f1:

    st.info(
        """
🧠 AI Prediction

Predict diseases using
Machine Learning algorithms.
"""
    )

with f2:

    st.success(
        """
📄 Health Report

Generate instant
health reports.
"""
    )

with f3:

    st.warning(
        """
👨‍⚕ Doctor Suggestion

Get treatment
recommendations.
"""
    )

st.write("")
st.divider()

# ----------------------------
# Services
# ----------------------------

st.subheader("🏥 Our Services")

a, b, c = st.columns(3)

with a:
    st.image("https://img.icons8.com/color/96/stethoscope.png", width=70)
    st.write("Disease Prediction")

with b:
    st.image("https://img.icons8.com/color/96/heart-health.png", width=70)
    st.write("Health Reports")

with c:
    st.image("https://img.icons8.com/color/96/hospital-room.png", width=70)
    st.write("Doctor Recommendation")

st.write("")
st.divider()

# ----------------------------
# Footer
# ----------------------------

st.markdown(
    """
<div style='text-align:center;color:gray;'>

© 2026 MediPredict AI

Powered by FastAPI • Streamlit • Machine Learning

</div>
""",
    unsafe_allow_html=True,
)