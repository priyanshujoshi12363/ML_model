from fastapi import FastAPI
from schemas.request import IndraInput
from model.indra import predict_indra
from schemas.request import DhanInput
from model.dhan import predict_dhan
from model.kavach import predict_kavach
from schemas.request import KavachInput
from pipeline.pipeline import run_pipeline
app = FastAPI(title="GigGuard AI ")

@app.get("/")
def home():
    return {"message": "Server running "}


@app.post("/api/indra")
def indra_api(data: IndraInput):
    result = predict_indra(data.dict())
    return result


@app.post("/api/dhan")
def dhan_api(data: DhanInput):
    return predict_dhan(data.dict())

@app.post("/api/kavach")
def kavach_api(data: KavachInput):
    return predict_kavach(data.dict())

@app.post("/api/predict")
def predict(data: dict):
    return run_pipeline(data)