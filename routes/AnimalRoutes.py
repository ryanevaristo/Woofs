from typing import Optional
from fastapi import APIRouter, Depends
from schema.AnimalSchema import Animal as SchemaAnimal
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from services.AnimalService import Animal as ServiceAnimal

router = APIRouter()

@router.post("/animal/", response_model=SchemaAnimal)
async def criar_animal(animal: SchemaAnimal, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceAnimal(dbSession)
    return await service.criar(animal)
    
@router.put("/animal/{id}", response_model=SchemaAnimal)
async def atualizar_animal(id: int, animal: SchemaAnimal, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceAnimal(dbSession)
    return await service.atualizar(animal, id)

@router.get("/animal/")
async def get_animal(id: Optional[int] = None, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceAnimal(dbSession)
    return await service.listar(id)
    
@router.delete("/animal/{id}")
async def delete_animal(id: int, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceAnimal(dbSession)
    return await service.remover(id)
