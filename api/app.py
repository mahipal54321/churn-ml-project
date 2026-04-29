from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import pandas as pd

# Create app
app = FastAPI(title="Churn Prediction API")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Load trained model
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
columns = joblib.load(os.path.join(BASE_DIR, "columns.pkl"))

# Define input schema (VERY IMPORTANT)
class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    SeniorCitizen: int
    Partner: str
    Dependents: str
    PhoneService: str
    InternetService: str
    Contract: str


@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}


@app.post("/predict")
def predict(data: CustomerData):
    try:
        input_dict = data.dict()
        df = pd.DataFrame([input_dict])

        # Convert Yes/No fields
        df['Partner'] = df['Partner'].map({'Yes': 1, 'No': 0})
        df['Dependents'] = df['Dependents'].map({'Yes': 1, 'No': 0})
        df['PhoneService'] = df['PhoneService'].map({'Yes': 1, 'No': 0})

        # One-hot encode categorical fields
        df = pd.get_dummies(df)

        # Create full feature set
        full_df = pd.DataFrame(columns=columns)

        for col in df.columns:
            if col in full_df.columns:
                full_df[col] = df[col]

        full_df = full_df.fillna(0)

        # Prediction
        prediction = model.predict(full_df)[0]
        prob = model.predict_proba(full_df)[0][1]

        return {
            "churn_prediction": int(prediction),
            "churn_probability": round(float(prob), 2)
        }

    except Exception as e:
        return {"error": str(e)}
        