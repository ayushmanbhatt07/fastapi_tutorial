from fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books=[
      {
        "id" : 1, 
        "title" : "The Alchemist", 
        "author" : "Paulo Coelho", 
        "publish_date" : "1988-01-01"
    },
    {
        "id" : 2, 
        "title" : "The God of Small Things", 
        "author" : "Arundhati Roy", 
        "publish_date" : "1997-04-04"
    },
    {
        "id" : 3, 
        "title" : "The White Tiger", 
        "author" : "Aravind Adiga", 
        "publish_date" : "2008-01-01"
    },
    {
        "id" : 4, 
        "title" : "The Palace of Illusions", 
        "author" : "Chitra Banerjee Divakaruni", 
        "publish_date" : "2008-02-12"
    },
]

app=FastAPI()

#fetching all the data from the list
@app.get("/books")
def get_book():
    return books

@app.get("/book/{book_id}")
def get_book(book_id:int):
    for book in books:
        if (book['id']==book_id):
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=
                        "book not found")

#post Request complete
#creating pydantic class for post method
class My_Books(BaseModel):
    id:int
    title:str
    author:str
    publish_date:str

@app.post("/book")
def create_book(book:My_Books):
    new_book=book.model_dump()
    books.append(new_book)

#updating data using put method
#creating pydantic class for update method
class My_Books_update(BaseModel):
    title:str
    author:str
    publish_date:str

@app.put("/book/{book_id}")
def update_book(book_id:int,book_update:My_Books_update):
    for book in books:
        if book['id']==book_id:
            book['title']=book_update.title
            book['author']=book_update.author
            book['publish_date']=book_update.publish_date
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book was not found, wrong book id")

#using DELETE method:
@app.delete("/book/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return {"Message":"Your book has been deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book was not found, wrong book id")