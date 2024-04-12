from typing import Union
from typing import Union

from fastapi import FastAPI

app = FastAPI()

user_id = "minju"

@app.get("/users/{user_id}")
async def read_user(user_id: int, q: str = None):
    return {"user_id": user_id, "q": q}


@app.post("/users/")
async def create_user(q: str = None):
    return {"q": q}

@app.put("/users/{user_id}")
async def update_user(user_id: int, q: str = None):
    return {"user_id": user_id, "q": q}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"user_id": user_id}