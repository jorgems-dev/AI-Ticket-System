from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.schemaUsuario import UsuarioResponse, UsuarioCreate, UsuarioUpdate, UsuarioLogin
from app.schemas.schemaComun import Message
from app.models.usuario import Usuario

router = APIRouter(prefix = "/usuarios", tags = ["Usuarios"])

# Crea un usuario nuevo
@router.post("/", response_model = UsuarioResponse, status_code = status.HTTP_201_CREATED)
async def crear_ticket(usuario: UsuarioCreate, db: Session = Depends(get_db)) -> Usuario:
    usuario_existe = db.query(Usuario).filter(Usuario.correo == usuario.correo).first()

    if usuario_existe:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = "Ya existe un usuario con ese correo. ")

    usuario_nuevo = Usuario(**usuario.model_dump())

    db.add(usuario_nuevo)
    db.commit()
    db.refresh(usuario_nuevo)

    return usuario_nuevo

# Devuelve una lista de usuarios
@router.get("/", response_model = list[UsuarioResponse])
async def get_list_usuarios(db: Session = Depends(get_db)) -> list[Usuario]:
    return db.query(Usuario).all()

# Devuelve un usuario buscado por su ID
@router.get("/{id_usuario}", response_model = UsuarioResponse)
async def get_usuario(id_usuario: int ,db: Session = Depends(get_db)) -> Usuario:
    usuario = db.get(Usuario, id_usuario)

    if not usuario:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Usuario no encontrado en la base de datos. ")
    
    return usuario

# ** Módificar ** metodo mal creado.
@router.post("/login", response_model = UsuarioResponse)
async def login_usuario(datos: UsuarioLogin, db: Session = Depends(get_db)):
    log_usuario = db.get(Usuario, correo, password)

    if not log_usuario:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Usuario no registrado en la base de datos con esos credenciales. ")

    return log_usuario

# Cambia o actualiza los campos de los usuarios buscados por su ID
@router.put("/{id_usuario}", response_model = UsuarioResponse)
async def update_usuario(id_usuario: int, datos: UsuarioUpdate, db: Session = Depends(get_db)) -> Usuario:
    usuario = db.get(Usuario, id_usuario)

    if not usuario:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Usuario no encontrado en la base de datos. ")

    for campo, valor in datos.model_dump(exclude_unset = True).items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)

    return usuario

# Borrar un usuario por su ID
@router.delete("/{id_usuario}", response_model = Message)
async def delete_usuario(id_usuario: int, db: Session = Depends(get_db)) -> Message:
    usuario = db.get(Usuario, id_usuario)

    if not usuario:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Usuario no encontrado en la base de datos. ")

    db.delete(usuario)
    db.commit()

    return Message(mensaje = "Usuario eliminado con éxito. ")