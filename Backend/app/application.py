import app as App

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.sport_objects import router as spo_router
from app.setup import router as setup_router
from app.container import ProjectContainer


origins = [
    "http://localhost:3000",
]

def create_app() -> FastAPI:
    container = ProjectContainer()
    container.wire(packages=[App], modules=[App])

    app = FastAPI()
    app.container = container
    app.include_router(setup_router)
    app.include_router(spo_router, prefix="/sport-objects")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["GET"],
        allow_headers=["*"],
    )


    return app

project_app = create_app()


