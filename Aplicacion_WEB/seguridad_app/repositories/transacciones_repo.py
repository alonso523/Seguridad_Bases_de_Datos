from sqlalchemy.orm import Session
from datetime import date
from seguridad_app.models.transaccion import Transaccion, Categoria

def obtener_categorias(db: Session):
    return db.query(Categoria).all()

def obtener_transacciones(db: Session):
    return db.query(Transaccion).all()

def obtener_transaccion_por_id(db: Session, transaccion_id: int):
    return db.query(Transaccion).filter(Transaccion.id == transaccion_id).first()

def crear_transaccion(db: Session, data):
    if not data.get("fecha"):
        data["fecha"] = date.today()

    if not data.get("tipo"):
        data["tipo"] = "gasto"

    nueva = Transaccion(**data)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def actualizar_transaccion(db: Session, transaccion_id: int, data):
    transaccion = obtener_transaccion_por_id(db, transaccion_id)
    if not transaccion:
        return None
    for key, value in data.items():
        setattr(transaccion, key, value)
    db.commit()
    db.refresh(transaccion)
    return transaccion

def eliminar_transaccion(db: Session, transaccion_id: int):
    transaccion = obtener_transaccion_por_id(db, transaccion_id)
    if not transaccion:
        return None
    db.delete(transaccion)
    db.commit()
    return True