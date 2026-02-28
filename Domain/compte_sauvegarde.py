
from Domain.compte import Compte
from abc import ABC, abstractmethod

class CompteSauvegarde(ABC):

    @abstractmethod
    def save(self, compte: Compte):
        pass

    @abstractmethod
    def get_by_id(self, identifier: str):
        pass

    @abstractmethod
    def exists(self,identifier: str):
        pass

