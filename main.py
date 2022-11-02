# Correr los siguientes comandos:
#   pip install "uvicorn[standard]"
#   pip install fastapi
#   pip install pydantic

# Para correr el servidor:
#   uvicorn main:app --reload

from typing import Union
from django.http import FileResponse

import pandas as pd
from fastapi import FastAPI
from joblib import load

from DataModel import DataModel
from PredictionModel import PredictionModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def make_prediction(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(),
                      columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    prediction_model = PredictionModel()
    results = prediction_model.make_prediction(df)
    return results.tolist()
