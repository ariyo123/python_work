from typing import Union
from fastapi import FastAPI, Path, Body,Query
from enum import Enum

app = FastAPI()
#a class to enforce only two entries ( limiting it to standard and admin) in the path operation
class UserType(str,Enum):
    STANDARD="standard"
    ADMIN="admin"

@app.get("/users/{name}/{id}/")
async def get_userE( name: UserType,id:int=Path(..., ge=2)): #pass the parameter as UserType to inherite the only two parameters allowed
    return {"type":name,"id":id}

@app.get("/")
async def hello_world():
    return {"hello": "world"}

@app.get("/users/{id}")
async def get_id(id:int=Path(..., ge=10)):
    return {"id":id}


@app.get("/users/{name}/{id}/")
async def get_user( name: str,id:int):
    return {"name":name,"id":id}



# @app.get("/license-plates/{license}")
# async def get_license_plate( license: str=Path(...,min_length=9,max_length=9)):
#     return {"license":license}

#advance validation using regex to ensure the path operation only accepts strings in this format xx-xxx-xx
#  Here is a breakdown of the regular expression:

# ^ is a start-of-line anchor that matches the position at the beginning of a line 
# \w is a shorthand character class that matches any word character (letter, digit, or underscore)
# {2} is a quantifier that specifies that the preceding character or group should be matched exactly 2 times
# - is a literal hyphen character
# \d is a shorthand character class that matches any digit
# $ is an end-of-line anchor that matches the position at the end of a line
# This regular expression would match strings like AB-123-CD, but would not match strings like AB-1234-CD (because it requires exactly 3 digits) or AB--CD (because it requires a hyphen followed by exactly 3 digits).
# Regenerate response

@app.get("/license-plates/{license}")
async def get_license_plates( license: str=Path(...,regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license":license}

#To enforce that the first digit of a string must be 2, you can use the following regular expression: ^2\d* 
# but if you want it to start with just digit 3 only use ^2\d{0}
@app.get("/license-platess/{license}")
async def get_license_platess( license: str=Path(...,regex=r"^2\d{0}-\d{3}-\w{2}$")):
    return {"license":license}


@app.post("/users")
async def create_user( name: str=Body(...,min_length=2,max_length=2), age:str=Body(...,regex=r"^2\d{1}$")):
    return {"name":name, "age":age}

#the Pydentic Approch to validation of fields

from pydantic import BaseModel

class User(BaseModel):
    name=str
    age=int

app=FastAPI()
@app.post("/users1")
async def create_user(user:User):
    return user
