from pydantic import BaseModel

class Localidade(BaseModel):
    longitude: float
    latitude: float
    limiteDistanciaMatch: int

    class Config:
        orm_mode = True