from fastapi import Form
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from seguridad_app.config.database import get_db
from seguridad_app.repositories.transacciones_repo import (obtener_transacciones, crear_transaccion, actualizar_transaccion, eliminar_transaccion, obtener_transaccion_por_id, obtener_categorias)


app = FastAPI()
templates = Jinja2Templates(directory="seguridad_app/templates")

# Listar las transacciones
@app.get("/transacciones", response_class=HTMLResponse)
def listar_transacciones(request: Request, db: Session = Depends(get_db)):
    transacciones = obtener_transacciones(db)
    return templates.TemplateResponse(
        "transacciones.html",
        {"request": request, "transacciones": transacciones}
    )

# Crear transacciones por medio del form
@app.get("/transacciones/crear", response_class=HTMLResponse)
def form_crear_transaccion(request: Request, db: Session = Depends(get_db)):
    categorias = obtener_categorias(db)
    return templates.TemplateResponse(
        "crear_transaccion.html",
        {"request": request, "categorias": categorias}
    )

@app.post("/transacciones/crear")
def crear_transaccion_post(
    request: Request,
    db: Session = Depends(get_db),
    monto: float = Form(...),
    descripcion: str = Form(...),
    categoria_id: int = Form(...)
):
    crear_transaccion(db, {
        "monto": monto,
        "descripcion": descripcion,
        "categoria_id": categoria_id
    })
    return RedirectResponse("/transacciones", status_code=303)

# Editar transacciones
@app.get("/transacciones/{id}/editar", response_class=HTMLResponse)
def form_editar_transaccion(id: int, request: Request, db: Session = Depends(get_db)):
    transaccion = obtener_transaccion_por_id(db, id)
    return templates.TemplateResponse("editar_transaccion.html", {"request": request, "t": transaccion})

@app.post("/transacciones/{id}/editar")
def editar_transaccion_post(
    id: int,
    db: Session = Depends(get_db),
    monto: float = Form(...),
    descripcion: str = Form(...)
):
    actualizar_transaccion(db, id, {"monto": monto, "descripcion": descripcion})
    return RedirectResponse("/transacciones", status_code=303)

#Elminar transacciones
@app.get("/transacciones/{id}/eliminar")
def eliminar_transaccion_view(id: int, db: Session = Depends(get_db)):
    eliminar_transaccion(db, id)
    return RedirectResponse("/transacciones", status_code=303)
