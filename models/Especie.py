from sqlalchemy import Column, Integer, String

from base import Base

class Especie(Base):
    __tablename__="Especie"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(60), nullable=True)

    def __repr__(self) -> str:
        return super().__repr__(f"id={self.id}, nome={self.nome}")
