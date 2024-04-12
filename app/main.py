from typing import Union
from fastapi import FastAPI

app = FastAPI()

user_name = "minju"

@app.get("/")
def read_name():
    return {"name": user_name}