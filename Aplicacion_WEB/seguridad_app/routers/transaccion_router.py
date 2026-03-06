from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from seguridad_app.config.database import get_db
from seguridad_app.schemas.transaccion import TransaccionCreate, TransaccionResponse
from seguridad_app.controllers import transaccion_controller
router = APIRouter(prefix="/transacciones", tags=["Transacciones"])
@router.post("/", response_model=TransaccionResponse)
def crear(transaccion: TransaccionCreate, db: Session = Depends(get_db)):
    return transaccion_controller.crear_transaccion(db, transaccion)
@router.get("/", response_model=list[TransaccionResponse])
def listar(db: Session = Depends(get_db)):
    return transaccion_controller.obtener_transacciones(db)
@router.get("/{id}", response_model=TransaccionResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    return transaccion_controller.obtener_transaccion(db, id)
@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return transaccion_controller.eliminar_transaccion(db, id)
