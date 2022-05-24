from abc import ABC, abstractmethod

class ServiceInterface(ABC):

    @abstractmethod
    def criar(self):
        pass

    @abstractmethod
    def atualizar(self):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def remover(self):
        pass