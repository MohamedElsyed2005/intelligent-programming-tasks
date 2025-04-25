import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

def define_membership_functions():
    """Define fuzzy variables and membership functions for heart disease risk assessment."""
    
    # Input Variables
    age = ctrl.Antecedent(np.arange(20, 101, 1), 'age')
    sex = ctrl.Antecedent(np.arange(0, 2, 1), 'sex')
    cp = ctrl.Antecedent(np.arange(0, 4, 1), 'cp')
    trestbps = ctrl.Antecedent(np.arange(90, 201, 1), 'trestbps')
    chol = ctrl.Antecedent(np.arange(100, 401, 1), 'chol')
    fbs = ctrl.Antecedent(np.arange(0, 2, 1), 'fbs')
    restecg = ctrl.Antecedent(np.arange(0, 3, 1), 'restecg')
    thalach = ctrl.Antecedent(np.arange(60, 211, 1), 'thalach')
    exang = ctrl.Antecedent(np.arange(0, 2, 1), 'exang')
    oldpeak = ctrl.Antecedent(np.arange(0.0, 7.0, 0.1), 'oldpeak')
    slope = ctrl.Antecedent(np.arange(0, 3, 1), 'slope')
    ca = ctrl.Antecedent(np.arange(0, 4, 1), 'ca')
    thal = ctrl.Antecedent(np.arange(0, 4, 1), 'thal')

    # Output Variable
    risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk')

    # Membership functions for age
    age['young'] = fuzz.trimf(age.universe, [20, 30, 40])
    age['middle'] = fuzz.trimf(age.universe, [35, 50, 65])
    age['old'] = fuzz.trimf(age.universe, [60, 80, 100])

    # Membership functions for sex
    sex['male'] = fuzz.trimf(sex.universe, [0, 0, 1])
    sex['female'] = fuzz.trimf(sex.universe, [0, 1, 1])

    # Membership functions for risk
    risk['low'] = fuzz.trimf(risk.universe, [0, 25, 50])
    risk['medium'] = fuzz.trimf(risk.universe, [30, 50, 70])
    risk['high'] = fuzz.trimf(risk.universe, [60, 80, 100])

    return age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, risk

def compute_risk(age_val, sex_val, cp_val, trestbps_val, chol_val, fbs_val, restecg_val, thalach_val, exang_val, oldpeak_val, slope_val, ca_val, thal_val):
    """Compute heart disease risk using fuzzy inference system."""
    
    age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, risk = define_membership_functions()

    # Define fuzzy control system
    rule1 = ctrl.Rule(age['old'] & cp['2'] & chol['high'], risk['high'])
    rule2 = ctrl.Rule(age['middle'] & cp['1'] & thalach['low'], risk['medium'])
    rule3 = ctrl.Rule(age['young'] & cp['0'] & trestbps['low'], risk['low'])

    risk_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    simulation = ctrl.ControlSystemSimulation(risk_ctrl)

    # Set input values
    simulation.input['age'] = age_val
    simulation.input['sex'] = sex_val
    simulation.input['cp'] = cp_val
    simulation.input['trestbps'] = trestbps_val
    simulation.input['chol'] = chol_val
    simulation.input['fbs'] = fbs_val
    simulation.input['restecg'] = restecg_val
    simulation.input['thalach'] = thalach_val
    simulation.input['exang'] = exang_val
    simulation.input['oldpeak'] = oldpeak_val
    simulation.input['slope'] = slope_val
    simulation.input['ca'] = ca_val
    simulation.input['thal'] = thal_val

    # Compute the result
    simulation.compute()
    return simulation.output['risk']
