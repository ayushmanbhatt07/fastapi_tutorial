from fastapi import FastAPI,Depends
from database import get_db
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app=FastAPI()

class BookStore(BaseModel):
    id:int
    title:str
    author:str
    publish_date: str

@app.post("/books")
def create_book(book:BookStore, db: Session=Depends(get_db)):
    new_book= model.Book(id=book.id,title=book.title,author=book.author,publish_date=book.publish_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book