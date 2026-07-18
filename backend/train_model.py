import pandas as pd
import joblib
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# ---------------- Load Dataset ---------------- #
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATASET_PATH = os.path.join(BASE_DIR, "dataset", "disease_dataset.csv")

df = pd.read_csv(DATASET_PATH)

# ---------------- Features ---------------- #

X = df.drop("disease", axis=1)

y = df["disease"]

# ---------------- Label Encoding ---------------- #

encoder = LabelEncoder()

y = encoder.fit_transform(y)

# ---------------- Split ---------------- #

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ---------------- Train Model ---------------- #

model = RandomForestClassifier(
    n_estimators=500,
    max_depth=15,
    min_samples_split=5,
    random_state=42
)

model.fit(

    X_train,

    y_train

)

# ---------------- Accuracy ---------------- #

prediction = model.predict(X_test)

accuracy = accuracy_score(

    y_test,

    prediction

)

print(f"Accuracy : {accuracy*100:.2f}%")

# ---------------- Save ---------------- #

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODELS_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODELS_DIR, exist_ok=True)

joblib.dump(
    model,
    os.path.join(MODELS_DIR, "model.pkl")
)

joblib.dump(
    encoder,
    os.path.join(MODELS_DIR, "label_encoder.pkl")
)

print("✅ Model Saved Successfully")
print(X.shape)
print(df.columns.tolist())