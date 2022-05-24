from typing import Optional
from fastapi import Query
from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select
#from service import ServiceInterface
from models.Usuario import Usuario as ModelUsuario
from schema.UsuarioSchema import Usuario as SchemaUsuario

class Usuario():
    def __init__(self, db: Session):
        self.db = db

    async def criar(self, usuario: SchemaUsuario):
        db_usuario = ModelUsuario(nome=usuario.nome,
                                email=usuario.email,
                                senha=usuario.senha,
                                idade=usuario.idade,
                                id_localidade=usuario.id_localidade
                        
                    )
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)

        return db_usuario

    async def atualizar(self,  usuario: SchemaUsuario, id: int):
        usuarioAtualizar = (
            update(ModelUsuario)
            .where(ModelUsuario.id == id)
            .values(**usuario.dict())
            .execution_options(synchronize_session="fetch")
        )
        await self.db.execute(usuarioAtualizar)

        return usuario.dict()
    
    async def listar(self, id: Optional[int]):
        if(id):
            query = select(ModelUsuario).where(ModelUsuario.id == id)
            resultados = await self.db.execute(query)
            (resulto, ) = resultados.one()
            return resulto
        else:
            query = select(ModelUsuario)
            resultados = await self.db.execute(query)
            return resultados.scalars().all()
    
    async def remover(self, id: int):
        query = delete(ModelUsuario).where(ModelUsuario.id == id)
        await self.db.execute(query)

    async def obter_email(self, email: str):
        query = select(ModelUsuario).where(ModelUsuario.email == email)
        return self.db.execute(query)