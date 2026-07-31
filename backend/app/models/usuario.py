from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

from enum import Enum as PyEnum

class Rol(str, PyEnum):
    ADMIN = "ADMIN"
    EMPLEADO = "EMPLEADO"
    TECNICO = "TECNICO"

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    fecha_creacion_user = Column(DateTime(timezone=True), server_default=func.now())
    rol = Column(Enum(Rol), nullable=False)

    tickets_creados = relationship("Ticket", back_populates="creador", foreign_keys="Ticket.id_creador")
    tickets_asignados = relationship("Ticket", back_populates="tecnico", foreign_keys="Ticket.id_tecnico")