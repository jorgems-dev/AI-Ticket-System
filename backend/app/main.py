from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.database import Base, engine, create_database
from app.models.ticket import Ticket
from app.models.usuario import User

from app.routers import routerTicket

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database()
    Base.metadata.create_all(bind = engine)

    yield

app = FastAPI(title = "DeskAI", version = "1.0.0", lifespan=lifespan)

app.include_router(routerTicket.router)