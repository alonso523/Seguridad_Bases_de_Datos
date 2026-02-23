from sqlalchemy import Column, Integer, String, Float, Date
from seguridad_app.config.database import Base
class Transaccion(Base):
    __tablename__ = "transacciones"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255), nullable=False)
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    categoria = Column(String(100), nullable=False)
