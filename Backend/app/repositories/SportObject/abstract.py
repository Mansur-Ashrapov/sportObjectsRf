from databases import Database
from abc import ABC, abstractmethod



class SportObjectABC(ABC):
    def __init__(self, db: Database):
        self.db = db

    @abstractmethod
    async def get_all_point_objects(self):
        """Получить необходимые данные по всем объектам для отоброжения точек"""

    @abstractmethod
    async def get_all_by_id(self):
        """Получить всю информацию об объекте"""
    
    @abstractmethod
    async def get_full_finance_by_regions(self):
        """Получить все финансирование по регионам"""