
from typing import Optional
from providers import hash_provider
from fastapi import APIRouter, Depends, HTTPException, status
from models.Usuario import Usuario
from schema.UsuarioSchema import Usuario as SchemaUsuario
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from services.UsuarioService import Usuario as ServiceUsuario

router = APIRouter()


@router.post("/usuario/", response_model=SchemaUsuario)
async def create_usuario(usuario: SchemaUsuario, dbSession: AsyncSession = Depends(get_db)):
        usuario_cadastrado = ServiceUsuario(dbSession).obter_email(usuario.email)

        if usuario_cadastrado:
            raise HTTPException(status_code = 400, detail="Já existe um usuário com esse email.")

        usuario.senha = hash_provider.gerar_hash(usuario.senha)
        service = ServiceUsuario(dbSession)
        return await service.criar(usuario)


@router.put("/usuario/{id}", response_model=SchemaUsuario)
async def get_usuario(id: int, usuario: SchemaUsuario, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceUsuario(dbSession)
    return await service.atualizar(usuario, id)

@router.get("/usuario/")
async def get_usuarioId(id: Optional[int] = None, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceUsuario(dbSession)
    return await service.listar(id)
    
@router.delete("/usuario/{id}")
async def delete_usuario(id: int, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceUsuario(dbSession)
    return await service.remover(id)