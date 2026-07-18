import pandas as pd
import random

symptoms = [
    "fever","cough","fatigue","headache","vomiting","nausea",
    "chest_pain","breathing_difficulty","joint_pain","skin_rash",
    "itching","diarrhea","constipation","loss_of_appetite",
    "weight_loss","weight_gain","back_pain","muscle_pain",
    "sore_throat","runny_nose"
]

diseases = [
    "Common Cold",
    "Flu",
    "COVID-19",
    "Typhoid",
    "Malaria",
    "Diabetes",
    "Migraine",
    "Pneumonia",
    "Asthma",
    "Heart Disease"
]

rows = []

for i in range(5000):

    row = {}

    for symptom in symptoms:
        row[symptom] = random.randint(0,1)

    row["disease"] = random.choice(diseases)

    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv("disease_dataset.csv", index=False)

print("Dataset Created Successfully")
print(df.head())