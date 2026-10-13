from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city:str
    pincode:str

class User(BaseModel):
    name:str
    age:int
    email:str
    address:Address

   

@app.post("/create_user")

def create_user(user:User):
    return {
        'message':"user created successfully",
        "data":user
    }