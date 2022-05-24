from enum import unique
from sqlalchemy import Boolean, Column, Integer, ForeignKey, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.Localidade import Localidade
from base import Base

class Usuario(Base):
    __tablename__ = 'Usuario'
    schema='dbo'

    id = Column(Integer, primary_key = True, autoincrement = True,  index = True)
    nome = Column(String(50), nullable = False)
    email = Column(String(55), nullable = False)
    senha = Column(String(200), nullable = False)
    idade = Column(String(2), nullable = False)
    
    id_localidade = Column(Integer, ForeignKey('Localidade.id'))
    localidade = relationship('Localidade', back_populates="usuario")

    def __repr__(self) -> str:
        return super().__repr__(f"id={self.id}, nome={self.nome}, email={self.email}, senha={self.senha}, idade={self.idade}")