from fastapi import FastAPI
from pydantic import ColorError
from sqlalchemy import Boolean, Column, DateTime, Integer, ForeignKey, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from base import Base
from models.Usuario import Usuario
from models.Raca import Raca
from models.Especie import Especie

class Animal(Base):
    __tablename__ = 'Animal'
    schema='dbo'

    id = Column(Integer, primary_key =True, autoincrement=True, index=True)
    nome = Column(String(50), nullable=False)
    id_raca = Column(Integer, ForeignKey("Raca.id"))
    id_especie = Column(Integer, ForeignKey("Especie.id"))
    sexo = Column(String(1), nullable=False)
    idade = Column(String(2), nullable=False)
    vacinacao = Column(String(200), nullable=False)
    validacao_vacina = Column(Boolean)
    id_usuario = Column(Integer, ForeignKey('Usuario.id'))
    usuario = relationship("Usuario")
    especie = relationship("Raca")
    def __repr__(self) -> str:
        return super().__repr__(f"id={self.id}, nome={self.nome}, especie={self.id_especie}, raca={self.id_raca}, sexo={self.sexo}, idade={self.idade}, vacinacao={self.vacinacao}, validacao_vacinacao={self.vacinacao}, id_usuario={self.id_usuario}")