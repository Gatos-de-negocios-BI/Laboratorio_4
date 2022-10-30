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

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/predict")
def make_prediction(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(),
                      columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    model = load('assets/modelo.joblib')
    result = model.predict(df)
    return result
