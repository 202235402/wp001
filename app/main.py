from typing import Union
from fastapi import FastAPI

app = FastAPI()

user_name = "minju"

@app.get("/")
def read_name():
    return {"name": user_name}

@app.post("/")
def create_name():

    return {}

@app.put("/")
def update_name():

    return {}

@app.delete("/")
def delete_name():
    user_name = ""
    return {"nme": "has been deleted"}