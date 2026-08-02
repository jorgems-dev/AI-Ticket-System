from datetime import datetime
from pydantic import BaseModel
from app.models.ticket import Prioridad, Estado

class TicketBase(BaseModel):
    titulo: str
    descripcion: str

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    id_ticket: int
    prioridad: Prioridad
    estado: Estado
    fecha_creacion: datetime
    id_creador: int
    id_tecnico: int | None = None

    class Config:
        from_attributes = True    

class TicketUpdate(BaseModel):
    titulo: str | None = None
    descripcion: str | None = None 
    prioridad: Prioridad | None = None 
