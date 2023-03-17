from databases import Database
from abc import ABC, abstractmethod



class CuratorABC(ABC):
    def __init__(self, db: Database):
        self.db = db

    @abstractmethod
    async def get_by_id(self):
        pass