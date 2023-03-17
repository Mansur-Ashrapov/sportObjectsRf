from pydantic import BaseSettings


class ProjectSettings(BaseSettings):
    DATABASE_URL: str 


settings = ProjectSettings()