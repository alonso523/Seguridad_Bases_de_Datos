from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib
from sqlalchemy.orm import Session

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=sqlserver;"                       ## Cambio clave para hacer que funcione el Docker-compose
    "DATABASE=FinanzasDB;"
    "UID=finanzas_user;"
    "PWD=Finanzas2024*;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()