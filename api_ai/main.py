from time import time
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import pandas as pd
import pickle


app = FastAPI()
model = pickle.load(open("/home/yanis/Téléchargements/Projet chef d'oeuvre/api_ai/notebooks/mlruns/0/00b86de19af243328541a503787900f6/artifacts/logistic_regression_pipeline/model.pkl", 'rb'))

class Test(BaseModel):
    name: str
    
#'{"job":"housemaid","marital":"married","education":"basic.education","default":"no","housing":"no","loan":"no","contact":"telephone","month":"may","day_of_week":"mon","duration":261,"campaign":1,"pdays":999,"previous":0,"poutcome":"nonexistent","emp.var.rate":1.1,"cons.price.idx":93.994,"cons.conf.idx":-36.4,"euribor3m":4.857,"nr.employed":5191.0,"y":0,"age_group":"Group 3"}'

@app.post("/test")
def test(data: Test):
    print(data)
    return {"Hello": "churn"}


################# 


class Data(BaseModel):
    duration: int
    campaign: int
    pdays : int
    previous : int
    cons_price_idx : float
    cons_conf_idx : float

    job: str
    marital: str
    education: str
    default: str
    housing: str
    loan: str
    age_group: str


@app.get("/")
def read_root():
    return {"Hello": "churn"}

@app.post("/prediction")
def prediction(data: Data):
    req = data.json()
    data = pd.read_json(req, orient='index').transpose()
    data.rename(columns = {"cons_conf_idx": "cons.conf.idx", "cons_price_idx": "cons.price.idx"}, inplace=True)
    pred = model.predict(data)
    return {"pred": "Le client ne vas pas souscrire" if pred == [0] else "Le client va souscrire"}


if __name__ == "__main":
    uvicorn.run()