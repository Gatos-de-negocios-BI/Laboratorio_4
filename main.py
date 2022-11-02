# Correr los siguientes comandos:
#   pip install "uvicorn[standard]"
#   pip install fastapi
#   pip install pydantic

# Para correr el servidor:
#   uvicorn main:app --reload

from typing import List

import pandas as pd
from fastapi import FastAPI

from DataModel import DataModel, DataModelComplete
from PredictionModel import PredictionModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def make_prediction(dataModel: List[DataModel]):
    df = pd.DataFrame([x.dict() for x in dataModel])
    df.columns = dataModel[0].columns()
    prediction_model = PredictionModel()
    results = prediction_model.make_prediction(df)
    return results.tolist()


@app.post("/fit")
def fit(dataModelComplete: List[DataModelComplete]):
    df = pd.DataFrame([x.dict() for x in dataModelComplete])
    df.columns = dataModelComplete[0].columns()
    prediction_model = PredictionModel()
    prediction_model.fit(df)
    return {"message": "Modelo entrenado exitosamente",
            "R2": prediction_model.r2,
            "MSE": prediction_model.mse,
            }
