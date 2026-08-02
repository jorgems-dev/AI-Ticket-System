from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from schemas.schemaTicket import TicketResponse, TicketCreate, TicketUpdate, Message
from models.ticket import Ticket

router = APIRouter(prefix = "/tickets", tags = ["Tickets"])
# Crear ticket nuevo
@router.post("/", response_model = TicketResponse, status_code = status.HTTP_201_CREATED)
async def crear_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket_nuevo = Ticket(**ticket.model_dump())

    db.add(ticket_nuevo)
    db.commit()
    db.refresh(ticket_nuevo)

    return ticket_nuevo

@router.get("/tickets", response_model = list[TicketResponse])
async def get_list_ticket(db: Session = Depends(get_db)):
    return db.query(Ticket).all()

@router.get("/tickets/{id_ticket}", response_model = TicketResponse)
async def get_ticket(id_ticket: int ,db: Session = Depends(get_db)):
    ticket = db.get(Ticket, id_ticket)

    if not ticket:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Ticket no encontrado en la base de datos. ")
    
    return ticket

# Obtener ticket por su ID
@router.put("/tickets/{id_ticket}", response_model = TicketResponse)
async def update_ticket(id_ticket: int, datos: TicketUpdate, db: Session = Depends(get_db)):
    ticket = db.get(Ticket, id_ticket)

    if not ticket:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Ticket no encontrado en la base de datos. ")

    for campo, valor in datos.model_dump(exclude_unset = True).items():
        setattr(ticket, campo, valor)

    db.commit()
    db.refresh(ticket)

    return ticket

# Borrar ticket por su ID
@router.delete("/tickets/{id_ticket}", response_model = Message)
async def delete_ticket(id_ticket: int, db: Session = Depends(get_db)):
    ticket = db.get(Ticket, id_ticket)

    if not ticket:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Ticket no encontrado en la base de datos. ")

    db.delete(ticket)
    db.commit()

    return Message(mensaje = "Ticket eliminado con éxito. ")