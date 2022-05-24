from pydantic import BaseModel

class Raca(BaseModel):
    nome: str

    class Config():
        orm_mode = True