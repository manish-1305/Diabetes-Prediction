

import numpy as np
import pickle

import streamlit as st

loaded_model =  pickle.load(open('trained_model.sav','rb'))

@st.cache_data
def  dia_prediction(input_data):
  
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    
    if (prediction[0] == 0):
        return'The person is not diabetic'
    else:
        return'The person is diabetic'
        
        
def main():

    #Title    
    st.title("Diabetes Prediction Web App")
    
    #Getting input data from use
    

    choose = ["No" ,"Yes"]
    choose2 = ["Low","High"]
    age = st.text_input("Enter the Age")
    hypertension = st.selectbox("Hypertension value",choose)
    heart_disease = st.selectbox("Heart_disease",choose)
    bmi = st.text_input("BMI value")
    HbA1c_level = st.text_input("Enter the HbA1c_level value")
    blood_glucose_level = st.text_input("Enter the blood_glucose_level value")
    options = ["Male","Female","Other"]
    gender = st.selectbox("Gender",options)
    history = ["No Info","never","former","current","not current","ever"]
    smoking_history_numeric = st.selectbox("Choose smoking_history",history)
    
    if  hypertension == "No":
        hypertension_1 = 0
    else:
        hypertension_1 = 1

    if gender == "Male":
        numeric_gender = 1
    elif gender == "Female":
        numeric_gender = 0
    else:
        numeric_gender = 2

    if  heart_disease == "No":
        heart_disease_1 = 0
    else:
        heart_disease_1 = 1


    if smoking_history_numeric == "No Info":
        smoking_history_numeric_1 = 0
    elif smoking_history_numeric == "never":
        smoking_history_numeric_1 = 1
    elif smoking_history_numeric == "former":
        smoking_history_numeric_1 = 2
    elif smoking_history_numeric == "current":
        smoking_history_numeric_1 = 3
    elif smoking_history_numeric == "not current":
        smoking_history_numeric_1 = 4 
    else:
        smoking_history_numeric_1 = 5
        

           



    #code for prediction
    
    diagnosis = ''
    
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        values = [age,hypertension_1, heart_disease_1,bmi,HbA1c_level,blood_glucose_level,numeric_gender,smoking_history_numeric_1 ]
        for i in values:
            print(i, end = ',')
        diagnosis =  dia_prediction([age,hypertension_1, heart_disease_1,bmi,HbA1c_level,blood_glucose_level,numeric_gender,smoking_history_numeric_1 ])
    
    st.success(diagnosis)


    
    
if __name__ == '__main__':
    main()    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
