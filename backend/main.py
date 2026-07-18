from fastapi import FastAPI
from pydantic import BaseModel
from database import engine, SessionLocal
from models import Base, User
from schemas import Register, Login
from auth import hash_password, verify_password, create_access_token
from models import Base, User, PredictionHistory
import joblib
import os
import numpy as np

# ---------------- Database ---------------- #

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Disease Prediction API",
    version="1.0"
)

# ---------------- Load ML Model ---------------- #

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

model = None
encoder = None

try:
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    print("✅ ML Model Loaded")
except Exception as e:
    print("⚠ Model Not Loaded:", e)

# ---------------- Home ---------------- #

@app.get("/")
def home():

    return {
        "message": "Disease Prediction API Running"
    }

# ---------------- Register ---------------- #

@app.post("/register")
def register(user: Register):

    db = SessionLocal()

    try:

        existing = db.query(User).filter(
            User.email == user.email
        ).first()

        if existing:

            return {
                "message": "Email already exists"
            }

        new_user = User(

            name=user.name,

            email=user.email,

            password=hash_password(user.password),

            age=user.age,

            gender=user.gender

        )

        db.add(new_user)

        db.commit()

        return {
            "message": "User Registered Successfully"
        }

    finally:
        db.close()

# ---------------- Login ---------------- #

@app.post("/login")
def login(user: Login):

    db = SessionLocal()

    try:

        existing = db.query(User).filter(
            User.email == user.email
        ).first()

        if existing is None:

            return {
                "message": "Invalid Email"
            }

        if not verify_password(
            user.password,
            existing.password
        ):

            return {
                "message": "Invalid Password"
            }

        token = create_access_token(
            {
                "sub": existing.email
            }
        )

        return {

            "message": "Login Successful",

            "name": existing.name,

            "email": existing.email,

            "token": token

        }

    finally:
        db.close()

# ---------------- Prediction Schema ---------------- #

class PredictionRequest(BaseModel):

    email: str

    symptoms: list[int]

# ---------------- Predict API ---------------- #

@app.post("/predict")
def predict(data: PredictionRequest):

    if model is None or encoder is None:

        return {
            "message": "Model Not Loaded"
        }

    db = SessionLocal()

    try:

        user = db.query(User).filter(
            User.email == data.email
        ).first()

        if user is None:

            return {
                "message": "User Not Found"
            }

        symptoms = np.array(data.symptoms).reshape(1, -1)

        prediction = model.predict(symptoms)

        disease = encoder.inverse_transform(prediction)[0]

        confidence = 95

        doctor = "General Physician"

        diet = "Healthy Diet"

        precautions = [

            "Drink More Water",

            "Take Proper Rest",

            "Eat Healthy Food",

            "Consult Doctor"

        ]

        history = PredictionHistory(

            user_id=user.id,

            patient_name=user.name,

            symptoms=",".join(map(str, data.symptoms)),

            disease=disease,

            confidence=confidence,

            doctor=doctor,

            diet=diet

        )

        db.add(history)

        db.commit()

        return {

            "disease": disease,

            "confidence": confidence,

            "doctor": doctor,

            "diet": diet,

            "precautions": precautions

        }

    finally:

        db.close()
@app.get("/history/{email}")
def get_history(email: str):

    db = SessionLocal()

    try:

        user = db.query(User).filter(
            User.email == email
        ).first()

        if user is None:

            return []

        history = db.query(PredictionHistory).filter(
            PredictionHistory.user_id == user.id
        ).order_by(
            PredictionHistory.created_at.desc()
        ).all()

        data = []

        for item in history:

            data.append({

                "Date": item.created_at.strftime("%d-%m-%Y"),

                "Disease": item.disease,

                "Confidence": f"{item.confidence}%",

                "Doctor": item.doctor,

                "Diet": item.diet

            })

        return data

    finally:

        db.close()
@app.get("/latest-report/{email}")
def latest_report(email: str):

    db = SessionLocal()

    try:

        user = db.query(User).filter(
            User.email == email
        ).first()

        if user is None:
            return {}

        report = db.query(PredictionHistory).filter(
            PredictionHistory.user_id == user.id
        ).order_by(
            PredictionHistory.created_at.desc()
        ).first()

        if report is None:
            return {}

        return {

            "patient_name": report.patient_name,

            "age": user.age,

            "gender": user.gender,

            "disease": report.disease,

            "confidence": report.confidence,

            "doctor": report.doctor,

            "diet": report.diet,

            "date": report.created_at.strftime("%d-%m-%Y"),

            "precautions":[

                "Drink More Water",

                "Take Proper Rest",

                "Eat Healthy Food",

                "Consult Doctor"

            ]

        }

    finally:

        db.close()
@app.get("/profile/{email}")
def get_profile(email: str):

    db = SessionLocal()

    try:

        user = db.query(User).filter(
            User.email == email
        ).first()

        if user is None:

            return {}

        return {

            "name": user.name,

            "email": user.email,

            "age": user.age,

            "gender": user.gender

        }

    finally:

        db.close()
@app.put("/profile/{email}")
def update_profile(email: str, data: Register):

    db = SessionLocal()

    try:

        user = db.query(User).filter(
            User.email == email
        ).first()

        if user is None:

            return {"message": "User Not Found"}

        user.name = data.name
        user.age = data.age
        user.gender = data.gender

        db.commit()

        return {"message": "Profile Updated Successfully"}

    finally:

        db.close()
@app.get("/admin/dashboard")
def admin_dashboard():

    db = SessionLocal()

    try:

        total_users = db.query(User).count()

        total_predictions = db.query(PredictionHistory).count()

        history = db.query(PredictionHistory).order_by(
            PredictionHistory.created_at.desc()
        ).all()

        diseases = {}

        recent = []

        for item in history:

            diseases[item.disease] = diseases.get(item.disease,0)+1

            recent.append({

                "Patient":item.patient_name,

                "Disease":item.disease,

                "Confidence":item.confidence,

                "Doctor":item.doctor,

                "Date":item.created_at.strftime("%d-%m-%Y")

            })

        return{

            "total_users":total_users,

            "total_predictions":total_predictions,

            "diseases":diseases,

            "recent":recent

        }

    finally:

        db.close()