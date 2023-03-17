from sqlalchemy.sql import text

from app.repositories.SportObject.abstract import SportObjectABC
from app.database.models import SportObject
from app.schemas.sport_objects import (
    SportObjectFull,
    SportObjectPoint
)
from app.repositories.SportObject.utils import regions

class SportObjectRepo(SportObjectABC):
    async def get_all_by_id(self, id: int, lang: str) -> SportObjectFull:
        query = SportObject.select().where(SportObject.c.id == id)
        req = await self.db.fetch_one(query)
        res = SportObjectFull.from_orm(req)

        if req == None or req.coor_x == None:
            return None

        if lang == "en" and req.name_en != None:
            res.name = req.name_en
            res.address = req.address_en
            res.detail_description = req.detail_description_en
            res.short_description = req.short_description_en
            res.city = req.city_en
        else:
            res.name = req.name_ru
            res.address = req.address_ru
            res.detail_description = req.detail_description_ru
            res.short_description = req.short_description_ru
            res.city = req.city_ru
        return res
    
    async def get_all_point_objects(self, lang: str) -> list[SportObjectPoint]:
        query = text("""SELECT id, is_active, coor_x, coor_y, name_ru, name_en FROM sport_objects WHERE is_active=true""")
        req = await self.db.fetch_all(query)

        if req == []:
            return None
        
        sport_objects = []
        for item in req:
            if item.coor_x is not None:
                obj = SportObjectPoint.from_orm(item)
                if lang == "en" and item.name_en != None:
                    obj.name = item.name_en
                else:
                    obj.name = item.name_ru
                sport_objects.append(obj)
            
        return sport_objects

    async def get_full_finance_by_regions(self):
        query = text("""SELECT sum(full_finance) AS sum, subject_of_federation FROM sport_objects WHERE is_active=true GROUP BY subject_of_federation""")
        req = await self.db.fetch_all(query)

        if req == None:
            return None

        res = {r:{k: 0 for k in regions[r]} for r in regions.keys()}   
        for region, value in res.items():
            for key in value.keys():
                for row in req:
                    if row.subject_of_federation == key:
                        res[region][key] = row.sum
        return res