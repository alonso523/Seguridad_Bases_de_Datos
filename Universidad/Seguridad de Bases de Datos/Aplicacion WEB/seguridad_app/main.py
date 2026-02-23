""" from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/index")
def pagina_web(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "titulo": "Mi primera página"}) """

from fastapi import FastAPI
from seguridad_app.config.database import Base, engine
from seguridad_app.routers import transaccion_router
# Crear tablas
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Finanzas Personales")
app.include_router(transaccion_router.router)
@app.get("/")
def root():
    return {"mensaje": "API de Finanzas Personales funcionando"}
