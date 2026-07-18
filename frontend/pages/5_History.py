import streamlit as st
import pandas as pd
import requests
from pathlib import Path

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
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
    st.switch_page("pages/3_Dashboard.py")

if st.sidebar.button("🤒 Disease Prediction"):
    st.switch_page("pages/4_Disease_Prediction.py")

if st.sidebar.button("📄 Report"):
    st.switch_page("pages/6_Report.py")

if st.sidebar.button("👤 Profile"):
    st.switch_page("pages/7_Profile.py")

if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.switch_page("pages/1_Login.py")

# ---------------- TITLE ---------------- #

st.title("📜 Prediction History")

st.write("View all your previous disease predictions.")

st.divider()

# ---------------- LOAD HISTORY ---------------- #

try:

    response = requests.get(

        f"http://127.0.0.1:8000/history/{st.session_state.user_email}"

    )

    history = pd.DataFrame(response.json())

except:

    history = pd.DataFrame()

# ---------------- SHOW HISTORY ---------------- #

if history.empty:

    st.info("No Prediction History Found.")

else:

    st.dataframe(

        history,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    c1,c2,c3=st.columns(3)

    with c1:

        st.metric(

            "Total Predictions",

            len(history)

        )

    with c2:

        st.metric(

            "Latest Disease",

            history.iloc[0]["Disease"]

        )

    with c3:

        st.metric(

            "Latest Confidence",

            history.iloc[0]["Confidence"]

        )

    csv = history.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download History",

        csv,

        "Prediction_History.csv",

        "text/csv",

        use_container_width=True

    )

st.divider()

st.markdown("""

<div style="text-align:center;color:gray">

© 2026 MediPredict AI

FastAPI • Streamlit • Machine Learning

</div>

""",unsafe_allow_html=True)