from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import Base, engine, create_database

from backend.app.models.usuario import User
from app.models.ticket import Ticket

@asynccontextmanager
async def lifespan():
    create_database()
    Base.metadata.create_all(bind=engine)

    yield

app = FastAPI(lifespan=lifespan)