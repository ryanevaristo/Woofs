from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.future import select
from services.service import ServiceInterface
from models.Localidade import Localidade as ModelLocalidade
from schema.LocalidadeSchema import Localidade as SchemaLocalidade


class Localidade():
    def __init__(self, db: Session):
        self.db = db

    async def criar(self, localidade: SchemaLocalidade):
        db_Localidade = ModelLocalidade(
            longitude=localidade.longitude,
            latitude=localidade.latitude,
            limiteDistanciaMatch=localidade.limiteDistanciaMatch
        )
        self.db.add(db_Localidade)
        self.db.commit()
        self.db.refresh(db_Localidade)
        return db_Localidade

    async def atualizar(self, localidade: SchemaLocalidade, id: int):
        LocalidadeAtualizar = (
            update(ModelLocalidade)
            .where(ModelLocalidade.id == id)
            .values(**localidade.dict())
            .execution_options(synchronize_session="fetch")
        )
        await self.db.execute(LocalidadeAtualizar)

        return localidade.dict()

    async def listar(self, id: Optional[int]):
        if (id):
            query = select(ModelLocalidade).where(ModelLocalidade.id == id)
            resultados = await self.db.execute(query)
            (resulto,) = resultados.one()
            return resulto
        else:
            query = select(ModelLocalidade)
            resultados = await self.db.execute(query)
            return resultados.scalars().all()
    def remover(self, id: int):
        return super().remover()