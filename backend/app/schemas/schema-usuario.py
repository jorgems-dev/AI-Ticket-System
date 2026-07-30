from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    nombre: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    fecha_creacion_user: datetime

    class Config:
        from_attributes = True