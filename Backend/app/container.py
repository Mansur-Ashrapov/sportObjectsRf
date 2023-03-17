from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import (
    Factory,
    Singleton
)
from databases import Database

from app.config import settings
from app.repositories import (
    CuratorRepo,
    SportObjectRepo
)


class ProjectContainer(DeclarativeContainer):
    wiring_config = WiringConfiguration(modules=["app"])

    database = Singleton(
        Database,
        url=settings.DATABASE_URL
    )

    sport_objects_repo = Factory(
        SportObjectRepo,
        db=database
    )
    curator_repo = Factory(
        CuratorRepo,
        db=database
    )
