# Correr los siguientes comandos:
#   pip install "uvicorn[standard]"
#   pip install fastapi
#   pip install pydantic

# Para correr el servidor:
#   uvicorn main:app --reload

from typing import List

import pandas as pd
from fastapi import FastAPI, HTTPException

from DataModel import DataModel, DataModelComplete
from PredictionModel import PredictionModel

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global prediction_model
    prediction_model = PredictionModel()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def make_prediction(dataModel: List[DataModel]):
    lista = []
    for x in dataModel:
        datos = x.dict()
        check_gre(datos['gre_score'])
        check_toefl(datos['toefl_score'])
        check_university_rating(datos['university_rating'])
        check_sop(datos['sop'])
        check_lor(datos['lor'])
        check_cpga(datos['cgpa'])
        check_research(datos['research'])
        lista.append(datos)
    df = pd.DataFrame(lista)
    df.columns = dataModel[0].columns()
    results = prediction_model.make_prediction(df)
    return results.tolist()
    
def check_gre(score:float):
    if score > 340 or score < 0:
        raise HTTPException(status_code=400, detail = "GRE debe ser menor o igual a 340 y mayor o igual a 0")

def check_toefl(score:float):
    if score > 120 or score < 0:
        raise HTTPException(status_code=400, detail = "TOEFL debe ser menor o igual a 120 y mayor o igual a 0")

def check_university_rating(score:float):
    if score > 5 or score < 0:
        raise HTTPException(status_code=400, detail = "University Rating debe ser menor o igual a 5 y mayor o igual a 0")

def check_sop(score:float):
    if score > 5 or score < 0:
        raise HTTPException(status_code=400, detail = "SOP debe ser menor o igual a 5 y mayor o igual a 0")

def check_lor(score:float):
    if score > 5 or score < 0:
        raise HTTPException(status_code=400, detail = "LOR debe ser menor o igual a 5 y mayor o igual a 0")

def check_cpga(score:float):
    if score > 10 or score < 0:
        raise HTTPException(status_code=400, detail = "CGPA debe ser menor o igual a 10 y mayor o igual a 0")

def check_research(score:float):
    if score > 1 or score < 0:
        raise HTTPException(status_code=400, detail = "Research debe ser 1 o 0")

@app.post("/fit")
def fit(dataModelComplete: List[DataModelComplete]):
    df = pd.DataFrame([x.dict() for x in dataModelComplete])
    df.columns = dataModelComplete[0].columns()
    prediction_model.fit(df)
    return {"message": "Modelo entrenado exitosamente",
            "R2": prediction_model.r2,
            "RMSE": prediction_model.rmse,
            }
