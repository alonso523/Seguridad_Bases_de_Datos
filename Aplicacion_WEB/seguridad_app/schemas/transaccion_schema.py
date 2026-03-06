from pydantic import BaseModel, constr, condecimal

class TransaccionCreate(BaseModel):
    monto: condecimal(gt=0)
    descripcion: constr(strip_whitespace=True, min_length=1, max_length=200)
    categoria_id: int

class TransaccionResponse(BaseModel):
    id: int
    monto: float
    descripcion: str
    categoria_id: int

    class Config:
        from_attributes = True