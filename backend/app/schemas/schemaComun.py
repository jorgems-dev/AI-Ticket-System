from pydantic import BaseModel

# Mensaje 
class Message(BaseModel):
    mensaje: str