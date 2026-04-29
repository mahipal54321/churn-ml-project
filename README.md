# Customer Churn Prediction System
## 🌍 Live Demo

- ML API: https://churn-ml-project.onrender.com/docs  
- UI: http://localhost:8501 (local)
## 📸 Demo Screenshot
<img width="896" height="832" alt="image" src="https://github.com/user-attachments/assets/e5b302b9-3f8b-44d2-9eda-e22d2fd17ecd" />

## 🚀 Overview

This project is an end-to-end machine learning system that predicts customer churn. It uses a Python-based ML model exposed via FastAPI and integrates it with a Java Spring Boot backend for real-time predictions.

## 🧠 Architecture

Client → Java (Spring Boot) → Python (FastAPI) → ML Model → Response

## 🛠 Technologies Used

* Python (FastAPI, scikit-learn, pandas)
* Java (Spring Boot)
* REST APIs
* Git & GitHub

## ▶️ How to Run Locally

### 1. Start Python ML API

cd churn-ml-project
venv\Scripts\activate
python -m uvicorn api.app:app --reload

Runs on:
http://127.0.0.1:8000

---

### 2. Start Java Backend

cd churn-ml-project/demo
.\mvnw.cmd spring-boot:run

Runs on:
http://localhost:8080

---

### 3. Test API (PowerShell)

Invoke-RestMethod -Uri "http://localhost:8080/churn/predict" -Method Post -ContentType "application/json" -Body '{"tenure":1,"MonthlyCharges":95.0,"TotalCharges":95.0,"SeniorCitizen":1,"Partner":"No","Dependents":"No","PhoneService":"Yes","InternetService":"Fiber optic","Contract":"Month-to-month"}'

---

## 📊 Example Output

churn_prediction : 1
churn_probability : 0.78

---

## 💡 Key Learnings

* Built a machine learning model for prediction
* Developed REST APIs using FastAPI
* Integrated ML with a Java backend
* Debugged real-world environment issues
* Learned Git and GitHub workflow

---

## 🌍 Deployment (Optional)

You can deploy the FastAPI app using platforms like Render:

* Build command: pip install -r requirements.txt
* Start command: uvicorn api.app:app --host 0.0.0.0 --port 10000

---

## 👨‍💻 Author

Mahipal Singh
