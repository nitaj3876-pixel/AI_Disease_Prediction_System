import streamlit as st
import requests
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Health Report",
    page_icon="📄",
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

st.sidebar.title("🩺 MediPredict AI")

st.sidebar.success(f"👋 {st.session_state.user_name}")

st.sidebar.markdown("---")

if st.sidebar.button("🏠 Dashboard"):
    st.switch_page("pages/3_Dashboard.py")

if st.sidebar.button("🤒 Disease Prediction"):
    st.switch_page("pages/4_Disease_Prediction.py")

if st.sidebar.button("📜 History"):
    st.switch_page("pages/5_History.py")

if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.switch_page("pages/1_Login.py")

# ---------------- TITLE ---------------- #

st.title("📄 AI Health Report")

st.write("Latest Prediction Report")

st.divider()

# ---------------- GET REPORT ---------------- #

try:

    response = requests.get(

        f"http://127.0.0.1:8000/latest-report/{st.session_state.user_email}"

    )

    report = response.json()

except:

    report = {}

# ---------------- NO DATA ---------------- #

if report == {}:

    st.info("No Report Available")

    st.stop()

# ---------------- DETAILS ---------------- #

col1,col2=st.columns(2)

with col1:

    st.subheader("👤 Patient Details")

    st.write(f"**Name :** {report['patient_name']}")

    st.write(f"**Age :** {report['age']}")

    st.write(f"**Gender :** {report['gender']}")

    st.write(f"**Date :** {report['date']}")

with col2:

    st.subheader("🩺 Prediction")

    st.success(report["disease"])

    st.write(f"**Confidence :** {report['confidence']}%")

    st.write(f"**Doctor :** {report['doctor']}")

st.divider()

st.subheader("🥗 Diet")

st.info(report["diet"])

st.divider()

st.subheader("💊 Precautions")

for p in report["precautions"]:

    st.write("✅",p)

# ---------------- PDF ---------------- #

def create_pdf():

    filename="Health_Report.pdf"

    doc=SimpleDocTemplate(filename)

    styles=getSampleStyleSheet()

    story=[]

    story.append(Paragraph("AI Disease Prediction Report",styles["Title"]))

    story.append(Paragraph(f"Patient : {report['patient_name']}",styles["Normal"]))

    story.append(Paragraph(f"Age : {report['age']}",styles["Normal"]))

    story.append(Paragraph(f"Gender : {report['gender']}",styles["Normal"]))

    story.append(Paragraph(f"Disease : {report['disease']}",styles["Normal"]))

    story.append(Paragraph(f"Confidence : {report['confidence']}%",styles["Normal"]))

    story.append(Paragraph(f"Doctor : {report['doctor']}",styles["Normal"]))

    story.append(Paragraph(f"Diet : {report['diet']}",styles["Normal"]))

    story.append(Paragraph("Precautions",styles["Heading2"]))

    for item in report["precautions"]:

        story.append(

            Paragraph(f"• {item}",styles["Normal"])

        )

    doc.build(story)

    return filename

# ---------------- DOWNLOAD ---------------- #

if st.button(

    "📄 Generate PDF",

    use_container_width=True

):

    pdf=create_pdf()

    with open(pdf,"rb") as f:

        st.download_button(

            "⬇ Download Report",

            f,

            file_name="Health_Report.pdf",

            mime="application/pdf",

            use_container_width=True

        )

st.divider()

st.markdown("""

<div style='text-align:center;color:gray'>

© 2026 MediPredict AI

FastAPI • Streamlit • Machine Learning

</div>

""",unsafe_allow_html=True)