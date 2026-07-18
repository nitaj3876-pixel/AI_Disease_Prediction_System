# 🩺 AI Disease Prediction System

A Professional AI-powered Disease Prediction Web Application built using **FastAPI**, **Streamlit**, **Machine Learning**, and **SQLite**.

---

# 📌 Project Overview

AI Disease Prediction System predicts possible diseases based on patient symptoms using a Machine Learning model.

The application provides secure login, disease prediction, health reports, prediction history, profile management, and an admin dashboard.

---

# 🚀 Features

## 👤 Patient

- Register
- Login
- Dashboard
- Disease Prediction
- Prediction History
- Download Health Report (PDF)
- Profile Management
- Logout

---

## 🛠 Admin

- Dashboard
- View Patient Records
- Disease Analytics
- Prediction Statistics
- Search Patient
- Delete Patient

---

# 🤖 Machine Learning

Algorithm Used

- Random Forest Classifier

Dataset

- Disease Prediction Dataset (CSV)

Model

- model.pkl
- label_encoder.pkl

---

# 🖥 Tech Stack

### Frontend

- Streamlit

### Backend

- FastAPI

### Database

- SQLite
- SQLAlchemy ORM

### Authentication

- JWT Authentication
- Password Hashing (bcrypt)

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Reports

- ReportLab (PDF)

---

# 📂 Project Structure

AI_Disease_Prediction_System

backend/
- main.py
- database.py
- models.py
- schemas.py
- auth.py

frontend/
- Home.py
- style.css

pages/
- Login
- Register
- Dashboard
- Disease Prediction
- Prediction History
- Health Report
- Profile
- Admin Dashboard

models/
- model.pkl
- label_encoder.pkl

dataset/
- disease_dataset.csv

assets/
- logo.png
- doctor.png
- profile.png

requirements.txt

README.md

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/yourusername/AI_Disease_Prediction_System.git
```

Open Project

```bash
cd AI_Disease_Prediction_System
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Install Packages

```bash
pip install -r requirements.txt
```

---

# ▶ Run Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

---

# ▶ Run Frontend

```bash
cd frontend

streamlit run Home.py
```

Frontend URL

```
http://localhost:8501
```

---

# 📊 Workflow

Patient Register

↓

Login

↓

Dashboard

↓

Select Symptoms

↓

Machine Learning Prediction

↓

Disease Result

↓

Health Report

↓

Prediction History

↓

Logout

---

# 📈 Future Improvements

- Doctor Appointment Booking
- Email Notifications
- Cloud Deployment
- Multi Disease Prediction
- Chatbot Integration
- Real-Time Analytics

---

# 📸 Screenshots

- Home Page
- Login Page
- Register Page
- Dashboard
- Disease Prediction
- Prediction History
- Health Report
- Admin Dashboard

(Add screenshots here)

---

# 👩‍💻 Developed By

**Nita Jadhav**

Diploma in Information Technology

---

# 📄 License

This project is created for educational and internship purposes.