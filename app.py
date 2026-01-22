from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    else:
        return "Overweight"

def get_plan(goal):
    if goal == "Muscle Gain":
        workout = [
            "Day 1: Chest + Triceps",
            "Day 2: Back + Biceps",
            "Day 3: Legs",
            "Day 4: Shoulders",
            "Day 5: Core + Light Cardio"
        ]
        diet = [
            "Breakfast: Eggs / Paneer + Oats",
            "Lunch: Rice/Roti + Dal + Vegetables",
            "Snack: Nuts + Fruits",
            "Dinner: Protein-rich meal"
        ]
        calories = "2800 – 3200 kcal/day"

    elif goal == "Maintain":
        workout = [
            "Day 1: Cardio (30 min)",
            "Day 2: Upper Body Strength",
            "Day 3: Lower Body Strength",
            "Day 4: Yoga / Stretching",
            "Day 5: Full Body Workout"
        ]
        diet = [
            "Breakfast: Oats / Poha + Fruits",
            "Lunch: Roti + Dal + Vegetables",
            "Snack: Fruits / Nuts",
            "Dinner: Light meal + Salad"
        ]
        calories = "2200 – 2600 kcal/day"

    else:  # Weight Loss
        workout = [
            "Day 1: HIIT",
            "Day 2: Cardio",
            "Day 3: Strength Training",
            "Day 4: Cardio + Core",
            "Day 5: Yoga / Stretching"
        ]
        diet = [
            "Breakfast: Fruits + Boiled Eggs",
            "Lunch: Salad + Protein",
            "Snack: Green Tea / Nuts",
            "Dinner: Light Soup / Veggies"
        ]
        calories = "1600 – 2000 kcal/day"

    return workout, diet, calories

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        height = float(request.form["height"])
        weight = float(request.form["weight"])

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        input_data = np.array([[age, height, weight, bmi]])
        pred = model.predict(input_data)
        goal = encoder.inverse_transform(pred)[0]

        workout, diet, calories = get_plan(goal)

        return render_template(
            "result.html",
            name=name,
            bmi=bmi,
            category=category,
            goal=goal,
            workout=workout,
            diet=diet,
            calories=calories
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

