from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select
from .service import ServiceInterface
from models.Animal import Animal as ModelAnimal
from schema.AnimalSchema import Animal as SchemaAnimal

class Animal(ServiceInterface):
    def __init__(self, db: Session):
        self.db = db
    async def criar(self, animal: SchemaAnimal):
        db_animal = ModelAnimal(nome=animal.nome, 
                        especie=animal.especie, sexo=animal.sexo,
                        raca=animal.raca, idade=animal.idade,
                        vacinacao=animal.vacinacao,
                        validacao_vacina=animal.validacao_vacina,
                        id_usuario=animal.id_usuario
                    )
        self.db.add(db_animal)
        await self.db.flush()

    async def atualizar(self,  animal: SchemaAnimal, id: int):
        animalAtualizar = (
            update(ModelAnimal)
            .where(ModelAnimal.id == id)
            .values(**animal.dict())
            .execution_options(synchronize_session="fetch")
        )
        await self.db.execute(animalAtualizar)

        return animal.dict()
    
    async def listar(self, id: Optional[int]):
        if(id):
            query = select(ModelAnimal).where(ModelAnimal.id == id)
            resultados = await self.db.execute(query)
            (resulto, ) = resultados.one()
            return resulto
        else:
            query = select(ModelAnimal)
            resultados = await self.db.execute(query)
            return resultados.scalars().all()
    
    async def remover(self, id: int):
        query = delete(ModelAnimal).where(ModelAnimal.id == id)
        await self.db.execute(query)

    
   
