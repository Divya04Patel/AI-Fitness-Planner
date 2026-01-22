import pandas as pd
import random

ROWS = 2000
data = []

for _ in range(ROWS):
    age = random.randint(18, 60)
    height_cm = random.randint(150, 190)
    height_m = height_cm / 100

    # Step 1: Choose BMI range deliberately
    category = random.choice(["Muscle Gain", "Maintain", "Weight Loss"])

    if category == "Muscle Gain":
        bmi = round(random.uniform(16.0, 18.4), 2)
    elif category == "Maintain":
        bmi = round(random.uniform(18.5, 24.9), 2)
    else:
        bmi = round(random.uniform(25.0, 32.0), 2)

    # Step 2: Compute weight from BMI
    weight_kg = round(bmi * (height_m ** 2), 1)

    data.append([age, height_cm, weight_kg, bmi, category])

df = pd.DataFrame(
    data,
    columns=["age", "height_cm", "weight_kg", "bmi", "fitness_goal"]
)

df.to_csv("data/fitness_dataset.csv", index=False)

print("✅ Dataset generated correctly")
print(df["fitness_goal"].value_counts())
