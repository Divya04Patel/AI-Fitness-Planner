# 🏋️‍♂️ AI Personalized Workout & Diet Planner

An AI-powered web application that provides **personalized workout schedules and diet plans** based on user body parameters such as age, height, weight, and BMI. The system uses **machine learning** to predict fitness goals and **rule-based intelligence** to generate structured plans.

---

## 📌 Project Overview

The **AI Personalized Workout & Diet Planner** helps users:
- Calculate their **BMI**
- Predict their **fitness goal** (Muscle Gain, Maintain, Weight Loss) using AI
- Receive a **day-wise workout plan**
- Receive a **meal-wise diet plan**
- Get recommended **daily calorie intake**

This project demonstrates a **hybrid AI system** combining:
- Machine Learning (Decision Tree Classifier)
- Rule-based planning
- Flask web framework

---

## 🧠 How the System Works

1. User enters personal details (age, height, weight)
2. BMI is calculated
3. A trained ML model predicts the **fitness goal**
4. Based on the predicted goal:
   - A **structured workout plan** is generated
   - A **structured diet plan** is generated
   - A **daily calorie range** is suggested
5. Results are displayed on a web interface

---

## ⚙️ Tech Stack

- **Frontend:** HTML, CSS  
- **Backend:** Python, Flask  
- **Machine Learning:** scikit-learn  
- **Data Handling:** pandas, numpy  
- **Model Storage:** joblib  

---
![WhatsApp Image 2026-01-22 at 21 56 46](https://github.com/user-attachments/assets/78341ea3-852c-434b-998e-18790502b2e9)

![WhatsApp Image 2026-01-22 at 21 56 46](https://github.com/user-attachments/assets/f2e2093a-b321-4e55-8503-f6b249fae1db)

---

## 📊 Dataset Description

The dataset is **synthetically generated** using realistic BMI ranges to ensure balanced classes.

### Features used:
- Age
- Height (cm)
- Weight (kg)
- BMI

### Target:
- Fitness Goal (`Muscle Gain`, `Maintain`, `Weight Loss`)

The dataset is generated programmatically to avoid bias and ensure proper learning.

---

## 🤖 Machine Learning Model

- **Algorithm:** Decision Tree Classifier
- **Input:** Age, Height, Weight, BMI
- **Output:** Fitness Goal
- **Reason for choice:**  
  - Easy to interpret  
  - Performs well on rule-based boundaries like BMI  

---

## 🥗 Workout & Diet Planning Logic

The AI model predicts **only the fitness goal**.  
Workout plans and diet plans are generated using **rule-based templates** based on this goal.

### Example:
- **Maintain**
  - Workout: Cardio + Strength (5-day plan)
  - Diet: Balanced meals
  - Calories: 2200–2600 kcal/day

This approach improves flexibility and avoids overfitting.

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install flask pandas numpy scikit-learn joblib

