from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("credit_model.pkl")
scaler = joblib.load("scaled.pkl")


class CreditData(BaseModel):
    LIMIT_BAL: float
    SEX: int
    EDUCATION: int
    MARRIAGE: int
    AGE: int
    PAY_1: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
    BILL_AMT1: float
    BILL_AMT2: float
    BILL_AMT3: float
    BILL_AMT4: float
    BILL_AMT5: float
    BILL_AMT6: float
    PAY_AMT1: float
    PAY_AMT2: float
    PAY_AMT3: float
    PAY_AMT4: float
    PAY_AMT5: float
    PAY_AMT6: float


@app.get("/")
def home():
    return {"message": "Credit Prediction API is running"}


@app.post("/predict")
def predict(data: CreditData):

    input_data = data.model_dump()

    df = pd.DataFrame([input_data])

    # Use the SAME scaler from training
    df_scaled = scaler.transform(df)

    prediction = model.predict(df_scaled)[0]

    probability = model.predict_proba(df_scaled)[0]

    if prediction == 1:
        result = "High risk of credit default"
    else:
        result = "Low risk of credit default"

    return {
        "prediction": int(prediction),
        "result": result,
        "default_probability": float(probability[1]),
        "no_default_probability": float(probability[0])
    }