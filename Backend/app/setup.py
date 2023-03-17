from databases import Database
from fastapi import APIRouter
from dependency_injector.wiring import Provide, inject

from app.container import ProjectContainer

router = APIRouter()


@router.on_event("startup")
@inject
async def startup(db: Database = Provide[ProjectContainer.database]):
    await db.connect()


@router.on_event("shutdown")
@inject
async def shutdown(db: Database = Provide[ProjectContainer.database]):
    await db.disconnect()
