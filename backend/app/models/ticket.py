from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base

from enum import Enum as PyEnum

class TypePrioridad(str, PyEnum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"
    URGENTE = "URGENTE"

class Ticket(Base):
    __tablename__ = "tickets"

    _id_ticket = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=False)
    prioridad = Column(Enum(TypePrioridad), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

    _id_creador = Column(Integer, ForeignKey("usuarios._id_usuario"), nullable=False)
    _id_tecnico = Column(Integer, ForeignKey("usuarios._id_usuario"), nullable=True)

    creador = relationship("Usuario", back_populates="tickets_creados", foreign_keys=[_id_creador])
    tecnico = relationship("Usuario", back_populates="tickets_asignados", foreign_keys=[_id_tecnico])