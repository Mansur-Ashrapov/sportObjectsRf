from datetime import datetime

from pydantic import BaseModel



class Curator(BaseModel):
    id: int
    phone: str | None = None
    name: str | None = None
    address: str | None = None