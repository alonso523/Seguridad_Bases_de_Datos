from pydantic import BaseModel
from datetime import date
class TransaccionBase(BaseModel):
    descripcion: str
    monto: float
    fecha: date
    categoria: str
class TransaccionCreate(BaseModel):
    descripcion: str
    monto: float
    fecha: date
    tipo: str
    categoria_id: int

class CategoriaResponse(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True
        
class TransaccionResponse(TransaccionBase):
    id: int
    descripcion: str
    monto: float
    fecha: date
    tipo: str
    categoria: CategoriaResponse

    class Config:
        orm_mode = True

