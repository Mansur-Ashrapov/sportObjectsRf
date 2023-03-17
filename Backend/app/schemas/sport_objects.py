import datetime

from pydantic import BaseModel


from app.schemas.curator import Curator


class SportObject(BaseModel):
    id: int
    is_active: bool
    coor_x: float
    coor_y: float

    class Config:
        orm_mode=True

class SportObjectPoint(SportObject):
    name: str | None = None

class SportObjectFull(SportObject):
    full_finance: float = 0
    name: str | None = None
    short_description: str | None = None
    detail_description: str | None = None
    address: str | None = None
    city: str | None = None
    phone: str | None = None
    type: str | None = None
    url: str | None = None
    kinds_of_sports: str | None = None
    email: str | None = None
    curator_id: int| None = None
    working_hours: str | None = None
    working_hours_sat: str | None = None
    area: str | None = None
    working_hours_sun: str | None = None
    municipality: str | None = None 
    subject_of_federation: str | None = None
    matter: str | None = None
    oktmo: str | None = None
    fcp: str | None = None
    action: str | None = None
    action_start_date: datetime.date | None = None
    action_compliton_date: datetime.date | None = None

class SportObjectOut(SportObjectFull):
    curator: Curator | None = None