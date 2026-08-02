from datetime import datetime
from pydantic import BaseModel, EmailStr
from app.models.ticket import Prioridad, Estado

class TicketBase(BaseModel):
    titulo: str
    descripcion: str
    prioridad: str

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    _id_ticket: int
    prioridad: Prioridad
    estado: Estado
    _id_creador: int
    _id_tecnico: int | None = None

    class Config:
        from_attributes = True    

class TicketUpdate(BaseModel):
    titulo: str | None = None
    descripcion: str | None = None 
    prioridad: Prioridad | None = None 

class Message(BaseModel):
    mensaje: str