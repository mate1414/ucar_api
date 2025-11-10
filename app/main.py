from fastapi import FastAPI

from app.core.config import settings
from app.core.routers import add_routers
from app.database import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version="1.0.0",
    docs_url="/docs",
)

add_routers(app)
