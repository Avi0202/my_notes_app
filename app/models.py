from sqlalchemy import Column,Integer,String
from .database import base
from pydantic import BaseModel

class Note(base):
    
    __tablename__="notes"
    id=Column(Integer, primary_key=True,index=True)
    title = Column(String,index=True)
    content=Column(String)
    
class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteInDB(NoteBase):
    id: int

    class Config:
        orm_mode = True