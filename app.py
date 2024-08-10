import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Function to load models with error handling
def load_model(model_name):
    # Construct the model path
    model_path = os.path.join(working_dir, 'artifacts', 'models', model_name)
    
    # Debugging output to check the model path
    print(f"Model path: {model_path}")  # Check the constructed path

    # Check if the model path exists
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            return pickle.load(file)
    else:
        st.error(f"{model_name} not found. Please check if the file exists in the specified path.")
        return None

# Loading the saved models
diabetes_model = load_model('diabetes.pkl')
heart_disease_model = load_model('heart_disease.pkl')
parkinsons_model = load_model('parkinsons.pkl')

# Check if models loaded successfully
if diabetes_model is None or heart_disease_model is None or parkinsons_model is None:
    st.stop()

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinsons Prediction"],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0)

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0)

    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0)

    with col3:
        BMI = st.number_input('BMI value', min_value=0.0)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0)

    with col2:
        Age = st.number_input('Age of the Person', min_value=0)

    # Prediction code
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=0)

    with col2:
        sex = st.number_input('Sex (1 = Male; 0 = Female)', min_value=0, max_value=1)

    with col3:
        cp = st.number_input('Chest Pain types', min_value=0)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0)

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0)

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)', min_value=0, max_value=1)

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results', min_value=0)

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0)

    with col3:
        exang = st.number_input('Exercise Induced Angina (1 = Yes; 0 = No)', min_value=0, max_value=1)

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0)

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment', min_value=0)

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy', min_value=0)

    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0)

    # Prediction code
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0)

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0)

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0)

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0)

    with col1:
        RAP = st.number_input('MDVP:RAP', min_value=0.0)

    with col2:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0)

    with col3:
        DDP = st.number_input('Jitter:DDP', min_value=0.0)

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0)

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0)

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0)

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0)

    with col3:
        APQ = st.number_input('MDVP:APQ', min_value=0.0)

    with col4:
        DDA = st.number_input('Shimmer:DDA', min_value=0.0)

    with col5:
        NHR = st.number_input('NHR', min_value=0.0)

    with col1:
        HNR = st.number_input('HNR', min_value=0.0)

    with col2:
        RPDE = st.number_input('RPDE', min_value=0.0)

    with col3:
        DFA = st.number_input('DFA', min_value=0.0)

    with col4:
        spread1 = st.number_input('spread1', min_value=0.0)

    with col5:
        spread2 = st.number_input('spread2', min_value=0.0)

    with col1:
        D2 = st.number_input('D2', min_value=0.0)

    with col2:
        PPE = st.number_input('PPE', min_value=0.0)

    # Prediction code
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)