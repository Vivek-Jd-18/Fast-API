from fastapi import FastAPI
from .router import user

app = FastAPI()
app.include_router(user.router)


"""
A simple function that returns a dictionary with a message "Hola Amigo!!!".
"""
@app.get('/')
def index():
    return {"message":"Hola Amigo!!!"}