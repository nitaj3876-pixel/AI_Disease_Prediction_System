from pydantic import BaseModel, EmailStr
from typing import List

# ---------------- Register Schema ---------------- #

class Register(BaseModel):

    name: str

    email: EmailStr

    password: str

    age: int

    gender: str


# ---------------- Login Schema ---------------- #

class Login(BaseModel):

    email: EmailStr

    password: str


# ---------------- Prediction ---------------- #

class PredictionRequest(BaseModel):

    symptoms: List[int]


# ---------------- Prediction Response ---------------- #

class PredictionResponse(BaseModel):

    disease: str

    confidence: int

    doctor: str

    diet: str

    precautions: List[str]


# ---------------- Profile ---------------- #

class Profile(BaseModel):

    name: str

    email: EmailStr

    age: int

    gender: str


# ---------------- History ---------------- #

class History(BaseModel):

    disease: str

    confidence: int

    date: str