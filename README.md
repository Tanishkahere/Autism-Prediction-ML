# 🩺 Autism Prediction System

A Machine Learning-based web application that estimates the likelihood of **Autism Spectrum Disorder (ASD)** using AQ-10 screening questionnaire responses and patient information.

The application provides an easy-to-use interface for early autism screening and presents the prediction along with confidence scores and recommendations.

> **Note:** This application is intended only for educational and screening purposes. It is **not** a medical diagnosis tool.

---

# Project Overview

Autism Spectrum Disorder (ASD) is a neurodevelopmental condition where early identification can significantly improve access to support and intervention.

This project combines Machine Learning with an interactive Streamlit web application to provide a quick autism screening experience based on behavioural questionnaire responses.

The application allows users to:

- Enter patient information
- Answer AQ-10 screening questions
- Receive an autism risk prediction
- View prediction confidence
- Review input summary
- Get recommendations based on the prediction

---

# Features

- Modern Streamlit web interface
- Machine Learning based prediction
- AQ-10 behavioural questionnaire
- Patient information form
- Prediction confidence score
- Probability distribution chart
- Assessment summary
- Responsive UI
- Professional dark theme

---

# Application Screenshots

## Home Page

![Home](images/images-home.png)

---

## Screening Questionnaire

![Questionnaire](images/images-questionnaire.png)

---

## Prediction Result

![Prediction](images/images-prediction.png)

---

# Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Joblib

### Data Processing

- Pandas
- NumPy

### Web Framework

- Streamlit

### Visualization

- Streamlit Charts

---

# Project Structure

```text
Autism-Prediction-ML/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── autism_screening.csv
│
├── models/
│   └── autism_app_model.pkl
│
├── notebooks/
│   ├── autism_prediction.ipynb
│   └── deployment_model.ipynb
│
└── images/
    ├── images-home.png
    ├── images-questionnaire.png
    └── images-prediction.png
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Tanishkahere/Autism-Prediction-ML.git
```

Move into the project

```bash
cd Autism-Prediction-ML
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
streamlit run app.py
```

The application will start locally in your browser.

---

# Dataset

The model is trained using an Autism Screening dataset containing:

- AQ-10 screening responses
- Age
- Gender
- Family history
- Jaundice history
- Previous screening history

---

# Machine Learning Model

The final prediction model was trained using Scikit-learn and exported using Joblib for deployment within the Streamlit application.

Model file:

```
models/autism_app_model.pkl
```

---

# Future Improvements

- Deploy the application on Streamlit Cloud
- Improve UI with interactive charts
- Add multilingual support
- Enhance model performance with additional data
- Store screening history
- PDF report generation
- User authentication

---

# Disclaimer

This application is intended solely for educational purposes and preliminary autism screening.

It **does not provide a medical diagnosis** and should not replace evaluation by qualified healthcare professionals.

---

# Author

**Tanishka Singh**

