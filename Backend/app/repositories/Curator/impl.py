from sqlalchemy.sql import text

from app.repositories.Curator.abstract import CuratorABC
from app.database.models import Curator
from app.schemas.curator import Curator as schema


class CuratorRepo(CuratorABC):
    async def get_by_id(self, id: int, lang: str) -> schema:
        query = Curator.select().where(Curator.c.id == id)
        req = await self.db.fetch_one(query)

        if req == None:
            return None

        if lang == "en" and req.name_en != None:
            return schema(
                id=req.id,
                phone=req.phone,
                name=req.name_en,
                address=req.address_en
            )
        return schema(
            id=req.id,
            phone=req.phone,
            name=req.name_ru,
            address=req.address_ru
        )
