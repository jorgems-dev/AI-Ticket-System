from datetime import datetime
from pydantic import BaseModel, EmailStr

class TicketBase(BaseModel):
    titulo: str
    