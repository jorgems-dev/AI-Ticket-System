from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from schemas.schemaTicket import TicketResponse, TicketCreate
from models.ticket import Ticket

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/tickets", response_model = TicketResponse, status_code = status.HTTP_201_CREATED)
async def crear_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket_nuevo = Ticket(**ticket.model_dump())

    db.add(ticket_nuevo)
    db.commit()
    db.refresh(ticket_nuevo)

    return ticket_nuevo

@app.get("/tickets", response_model = list[TicketResponse])
async def lista_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()

@app.get("/tickets/{id_ticket}", response_model = TicketResponse)
async def obtener_ticket_x_id(id_ticket: int ,db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id_ticket == id_ticket).first()

    if not ticket:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Ticket no encontrado en la base de datos. ")
    
    return ticket