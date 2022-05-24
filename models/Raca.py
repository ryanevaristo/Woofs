from tkinter.tix import COLUMN
from sqlalchemy import Column, Integer, String

from base import Base

class Raca(Base):
    __tablename__ = "Raca"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    nome = Column(String(60), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__(f"id={self.id}, nome={self.nome}")