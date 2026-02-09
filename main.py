from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()
#basic use
@app.get("/")
def read_root():
    return {"message": "Hello world"}
#end point
@app.get("/greet")
def greet():
    return {"message": "good morning"}
#passing path parameter
@app.get("/greet/{name}")
def greet_name(name:str):
    return {"Message":f"Hello {name}"}
#passing query parameter
@app.get("/greet2/{name}")
def greet_name_with_age(name:str,age:Optional[int]=None):
    return {"message":f"your name is {name} and age is {age}"}

#passing multiple query parameter
@app.get("/greet3/")
def greet_name_with_age(name:str,age:Optional[int]=None):
    return {"message":f"your name is {name} and age is {age}"}

class Student(BaseModel):
    name:str
    age:int
    roll:int

@app.post("/create_student")
def create_student(student:Student):
    return {
        "name":student.name,
        "AGE":student.age,
        "roll":student.roll
    }
