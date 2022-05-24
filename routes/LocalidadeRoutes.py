from fastapi import APIRouter, Depends

from schema.LocalidadeSchema import Localidade as SchemaLocalidade
from models.Localidade import Localidade as ModelLocalidade
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from database import db
from services.LocalidadeService import Localidade as ServiceLocalidade
from typing import Optional


router = APIRouter()


@router.post("/animal/localidade", response_model=SchemaLocalidade)
async def Create_Localidade(Localidade: SchemaLocalidade, dbSession: AsyncSession = Depends(db.get_db)):
    service = ServiceLocalidade(dbSession)
    return await service.criar(Localidade)


@router.get("/animal/localidade")
async def get_LocalidadeId(id: Optional[int] = None, dbSession: AsyncSession = Depends(db.get_db)):
    service = ServiceLocalidade(dbSession)
    return await service.listar(id)


@router.get("/animal/localidade{id}")
async def get_localidadeId(db: Session = Depends(db.get_db)):
    service = ServiceLocalidade(db)
    return await service.listar(id)