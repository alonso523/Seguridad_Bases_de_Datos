from pydantic import BaseModel
from datetime import date
class TransaccionBase(BaseModel):
    descripcion: str
    monto: float
    fecha: date
    categoria: str
class TransaccionCreate(TransaccionBase):
    pass
class TransaccionResponse(TransaccionBase):
    id: int
class Config:
        orm_mode = True
