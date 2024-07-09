from fastapi import FastAPI
from . import models
from .router import user

app = FastAPI()
app.include_router(user.router)

@app.get('/')
def index():
    return {"message":"Hola Amigo!!!"}