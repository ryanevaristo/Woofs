from pydantic import BaseModel, ValidationError, validator
from typing import Optional


class Animal(BaseModel):
    nome: str
    id_especie: int
    sexo: str
    id_raca: int
    idade: str
    vacinacao: str = None
    validacao_vacina: bool = None
    id_usuario: int

    # @validator('nome')
    # def nomeTemQueConterEspaco(cls, v):
    #     if ' ' in v:
    #         raise ValueError('001')
    #     return v.title()
        
    class Config:
        orm_mode = True