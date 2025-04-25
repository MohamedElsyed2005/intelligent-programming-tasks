"""
You are tasked with creating a Python program that uses fuzzy logic to assess the risk level of 
heart disease based on input parameters like 
age,
sex,
chest pain type (cp),
resting blood pressure (trestbps),
cholesterol level (chol),
fasting blood sugar (fbs),
resting ECG results (restecg),
maximum heart rate achieved (thalach),
exercise-induced angina (exang),
oldpeak (ST depression induced by exercise),
slope of the peak exercise ST segment (slope),
number of major vessels colored by fluoroscopy (ca),
and thalassemia type (thal).
The system should classify the risk as Low, Medium, or High based on fuzzy rules.
"""

from fuzzy_logic import compute_risk

def get_user_input():
    """Collects user input for heart disease risk assessment."""
    age = int(input("Enter age: "))
    sex = int(input("Enter sex (0 = female, 1 = male): "))
    cp = int(input("Enter chest pain type (0-3): "))
    trestbps = int(input("Enter resting blood pressure: "))
    chol = int(input("Enter cholesterol level: "))
    fbs = int(input("Enter fasting blood sugar (0 = False, 1 = True): "))
    restecg = int(input("Enter resting ECG results (0-2): "))
    thalach = int(input("Enter maximum heart rate achieved: "))
    exang = int(input("Enter exercise-induced angina (0 = No, 1 = Yes): "))
    oldpeak = float(input("Enter oldpeak: "))
    slope = int(input("Enter slope (0-2): "))
    ca = int(input("Enter number of major vessels (0-3): "))
    thal = int(input("Enter thalassemia type (0-3): "))
    
    return (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

def interpret_risk_level(risk_score):
    """Interpret the risk score into Low, Medium, or High risk levels."""
    if risk_score < 35:
        return "Low"
    elif risk_score < 70:
        return "Medium"
    else:
        return "High"

if __name__ == "__main__":
    user_data = get_user_input()
    risk_score = compute_risk(*user_data)
    risk_level = interpret_risk_level(risk_score)
    print(f"Heart Disease Risk Level: {risk_level}")
