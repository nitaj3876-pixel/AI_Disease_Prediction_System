import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from pathlib import Path

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛠",
    layout="wide"
)

# ---------------- CSS ---------------- #

css = Path("style.css")

if css.exists():
    st.markdown(
        f"<style>{css.read_text()}</style>",
        unsafe_allow_html=True
    )

# ---------------- LOGIN ---------------- #

if "logged_in" not in st.session_state:
    st.warning("Please Login First")
    st.stop()

# ---------------- SIDEBAR ---------------- #

st.sidebar.image("assets/logo.png", width=120)

st.sidebar.title("🛠 Admin Panel")

st.sidebar.success(st.session_state.user_name)

st.sidebar.markdown("---")

if st.sidebar.button("🏠 Dashboard"):
    st.switch_page("pages/3_Dashboard.py")

if st.sidebar.button("🤒 Prediction"):
    st.switch_page("pages/4_Disease_Prediction.py")

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

st.title("🛠 Admin Dashboard")

st.write("System Analytics")

st.divider()

# ---------------- LOAD DATA ---------------- #

try:

    response=requests.get(

        "http://127.0.0.1:8000/admin/dashboard"

    )

    data=response.json()

except:

    st.error("FastAPI Server Not Running")

    st.stop()

# ---------------- METRICS ---------------- #

c1,c2,c3=st.columns(3)

with c1:

    st.metric(

        "👥 Total Users",

        data["total_users"]

    )

with c2:

    st.metric(

        "🩺 Total Predictions",

        data["total_predictions"]

    )

with c3:

    st.metric(

        "🦠 Diseases",

        len(data["diseases"])

    )

st.divider()

# ---------------- PIE CHART ---------------- #

if len(data["diseases"])>0:

    df=pd.DataFrame({

        "Disease":list(data["diseases"].keys()),

        "Count":list(data["diseases"].values())

    })

    fig=px.pie(

        df,

        names="Disease",

        values="Count",

        title="Disease Distribution"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

st.divider()

# ---------------- RECENT TABLE ---------------- #

st.subheader("📜 Recent Predictions")

recent=pd.DataFrame(data["recent"])

if len(recent)>0:

    st.dataframe(

        recent,

        use_container_width=True,

        hide_index=True

    )

    csv=recent.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download CSV",

        csv,

        "Predictions.csv",

        "text/csv",

        use_container_width=True

    )

else:

    st.info("No Predictions Available")

st.divider()

st.markdown("""

<div style="text-align:center;color:gray">

© 2026 MediPredict AI

FastAPI • Streamlit • Machine Learning

</div>

""",unsafe_allow_html=True)