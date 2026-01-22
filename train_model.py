import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset from correct folder
df = pd.read_csv("data/fitness_dataset.csv")

X = df[["age", "height_cm", "weight_kg", "bmi"]]
y = df["fitness_goal"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
joblib.dump(encoder, "encoder.pkl")

print("✅ Model trained and saved successfully")
