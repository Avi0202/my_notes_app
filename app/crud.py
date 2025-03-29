from sqlalchemy.orm import Session
from . import models

def create_note_in_db(db: Session, note: models.NoteCreate):
    # Create a new Note instance using the Pydantic schema
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)  # Add the new note to the session
    db.commit()  # Commit the transaction to save the note in the database
    db.refresh(db_note)  # Refresh the instance to get the updated data from the database
    return db_note  # Return the newly created note

def get_notes(db: Session, skip: int = 0, limit: int = 10):
    # Query the database to get a list of notes, with optional pagination
    return db.query(models.Note).offset(skip).limit(limit).all()

def get_note_by_id(db: Session, note_id: int):
    # Query the database to get a single note by its ID
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def update_note_in_db(db: Session, note_id: int, note_update: models.NoteCreate):
    # Find the note by ID and update its title and content
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note:
        db_note.title = note_update.title
        db_note.content = note_update.content
        db.commit()  # Commit the transaction to save changes
        db.refresh(db_note)  # Refresh the instance to get the updated data
    return db_note

def delete_note_in_db(db: Session, note_id: int):
    # Find the note by ID and delete it from the database
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note:
        db.delete(db_note)  # Delete the note from the session
        db.commit()  # Commit the transaction to remove the note from the database
    return db_note