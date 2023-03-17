from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database

from app.database.models import metadata
from app.config import settings


engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata.create_all(engine)