from sqlalchemy import Numeric, Column, Integer, ForeignKey, String, Float
from base import Base
from sqlalchemy.orm import relationship

class Localidade(Base):
    __tablename__ = 'Localidade'
    schema='dbo'

    id = Column(Integer, primary_key = True, autoincrement = True,  index = True)
    longitude = Column(Numeric(9,6), nullable = False)
    latitude = Column(Numeric(9,6), nullable = False)
    limiteDistanciaMatch = Column(Integer, nullable = False)
    
    usuario = relationship("Usuario", back_populates="localidade", uselist=False)
    
    def __repr__(self) -> str:
        return super().__repr__(f"id={self.id}, longitude={self.longitude}, latitude={self.latitude}, limiteDistanciaMatch = {self.limiteDistanciaMatch}")

