from pydantic import BaseModel

class Especie(BaseModel):
    nome: str

    class Config():
        orm_mode=True
