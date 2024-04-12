from typing import Union
from fastapi import FastAPI

app = FastAPI()

user_name = "minju"

@app.get("/")
def read_name():
    return {"name": user_name}

@app.post("/")
def create_name(new_name: str):
    return {"name": new_name}

@app.put("/")
def update_name(updated_name: str):
    user_name = updated_name
    return {"name": user_name}

@app.delete("/")
def delete_name():
    user_name = ""
    return {"name": "has been deleted"}