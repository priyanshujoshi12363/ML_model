from fastapi import FastAPI
from schemas.request import IndraInput
from model.indra import predict_indra
app = FastAPI(title="GigGuard AI ")

@app.get("/")
def home():
    return {"message": "Server running "}


@app.post("/api/indra")
def indra_api(data: IndraInput):
    result = predict_indra(data.dict())
    return result