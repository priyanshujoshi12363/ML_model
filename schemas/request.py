from pydantic import BaseModel

class IndraInput(BaseModel):
    rain: float
    aqi: int
    wind: float
    visibility: float
    humidity: float
    temp: float
    pressure: float
    hour: int
    location_risk: int
    curfew: int