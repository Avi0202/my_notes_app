from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from . import crud, models
from .database import Sessionlocal, engine
from .config import templates

models.base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/addnote", response_class=HTMLResponse)
async def add_note_form(request: Request):
    return templates.TemplateResponse("add_note.html", {"request": request})

@router.post("/addnote")
async def add_note(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    note = models.NoteCreate(title=title, content=content)
    crud.create_note_in_db(db=db, note=note)
    return templates.TemplateResponse("add_note.html", {"request": request, "message": "Note added successfully!"})

@router.get("/notes", response_class=HTMLResponse)
async def read_notes(request: Request, db: Session = Depends(get_db)):
    notes = crud.get_notes(db)
    return templates.TemplateResponse("notes.html", {"request": request, "notes": notes})