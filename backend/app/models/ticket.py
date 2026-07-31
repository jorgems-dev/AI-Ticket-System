from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base

from enum import Enum as PyEnum

class Prioridad(str, PyEnum):
    BAJA = "Baja"
    MEDIA = "Media"
    ALTA = "Alta"
    URGENTE = "Urgente"

class Estado(str, PyEnum):
    CERRADO = "Cerrado"
    EN_PROCESO = "En proceso"
    PENDIENTE = "Pendiente"

class Ticket(Base):
    __tablename__ = "tickets"

    id_ticket = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=False)
    prioridad = Column(Enum(Prioridad), nullable=False)
    estado = Column(Enum(Estado), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

    id_creador = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_tecnico = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=True)

    creador = relationship("Usuario", back_populates="tickets_creados", foreign_keys=[id_creador])
    tecnico = relationship("Usuario", back_populates="tickets_asignados", foreign_keys=[id_tecnico])