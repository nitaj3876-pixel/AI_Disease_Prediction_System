from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# ==========================
# USER TABLE
# ==========================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, index=True, nullable=False)

    password = Column(String(255), nullable=False)

    age = Column(Integer, nullable=False)

    gender = Column(String(20), nullable=False)

    predictions = relationship(
        "PredictionHistory",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# ==========================
# PREDICTION HISTORY
# ==========================

class PredictionHistory(Base):

    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    patient_name = Column(String(100))

    symptoms = Column(String(500))

    disease = Column(String(100))

    confidence = Column(Float)

    doctor = Column(String(100))

    diet = Column(String(300))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="predictions"
    )