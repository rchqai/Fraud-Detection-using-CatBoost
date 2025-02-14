from fastapi import FastAPI
import pandas as pd
import joblib
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load trained model
model = joblib.load("catboost_model.pkl")

# Define request model
class Transaction(BaseModel):
    step: int
    type: int
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float

@app.post("/predict")
def predict(transaction: Transaction):
    data = pd.DataFrame([transaction.dict()])
    prediction = model.predict(data)
    return {"isFraud": int(prediction[0])}
