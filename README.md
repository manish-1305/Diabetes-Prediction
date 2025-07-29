# Diabetes Prediction Using Machine Learning

A machine learning project that predicts diabetes risk using Support Vector Machine (SVM) classification with an interactive Streamlit web application.

## 📊 Dataset
- **Size**: 100,000 patient records
- **Features**: Age, BMI, HbA1c level, blood glucose level, hypertension, heart disease, gender, smoking history
- **Target**: Binary classification (diabetic/non-diabetic)
- **Class Distribution**: 91,500 non-diabetic, 8,500 diabetic cases

## 🔧 Technical Implementation
- **Algorithm**: Support Vector Machine (SVM) with linear kernel
- **Data Preprocessing**: 
  - Categorical encoding (gender, smoking history)
  - Feature standardization using StandardScaler
  - Train-test split (80-20) with stratification
- **Performance**: 96% accuracy on test data
- **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn

## 🚀 Features
- **Jupyter Notebook**: Complete data analysis, preprocessing, model training, and evaluation
- **Streamlit App**: Interactive web interface for real-time diabetes risk prediction
- **Model Persistence**: Trained model saved using pickle for deployment
- **User-Friendly Interface**: Easy input form with instant predictions

## 📈 Model Performance
- **Training Accuracy**: 95.99%
- **Testing Accuracy**: 96.05%
- **Precision**: 92% for diabetic cases
- **Recall**: 60% for diabetic cases

## 🛠️ Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run Streamlit app: `streamlit run app.py`
4. Input patient data and get instant diabetes risk prediction

## App
![image](https://github.com/user-attachments/assets/c3a12546-241b-40ed-bead-09112d075bce)

## 📁 Project Structure
```
├── Diabetic_prediction_Project.ipynb  # Main analysis notebook
├── app.py                            # Streamlit web application
├── trained_model.sav                 # Saved SVM model
├── diabetes_prediction_dataset.csv   # Dataset
└── requirements.txt                  # Dependencies
```

Perfect for healthcare professionals, researchers, or anyone interested in medical machine learning applications.
