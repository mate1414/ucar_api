from fastapi import FastAPI

from app.api.routers import incident, source


def add_routers(app: FastAPI) -> None:
    app.include_router(incident.router, prefix="/api", tags=["incidents"])
    app.include_router(source.router, prefix="/api", tags=["sources"])
