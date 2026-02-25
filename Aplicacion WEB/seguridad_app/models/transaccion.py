from sqlalchemy import Column, Integer, String, Float, Date
from seguridad_app.config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

class Transaccion(Base):
    __tablename__ = "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255), nullable=False)
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    tipo = Column(String(20), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    categoria = relationship("Categoria")

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))