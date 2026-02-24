from sqlalchemy.orm import Session
from seguridad_app.models.transaccion import Transaccion
from seguridad_app.schemas.transaccion import TransaccionCreate
def crear_transaccion(db: Session, transaccion: TransaccionCreate):
    nueva = Transaccion(**transaccion.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva
def obtener_transacciones(db: Session):
    return db.query(Transaccion).all()
def obtener_transaccion(db: Session, transaccion_id: int):
    return db.query(Transaccion).filter(Transaccion.id == transaccion_id).first()
def eliminar_transaccion(db: Session, transaccion_id: int):
    trans = obtener_transaccion(db, transaccion_id)
    if trans:
        db.delete(trans)
        db.commit()
    return trans
