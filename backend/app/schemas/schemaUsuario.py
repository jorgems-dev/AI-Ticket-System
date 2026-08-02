from datetime import datetime
from pydantic import BaseModel, EmailStr
from app.models.usuario import Rol

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    rol: Rol
    fecha_creacion_user: datetime

    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    correo: EmailStr
    password: str

class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    correo: EmailStr | None = None
    password: str | None = None

