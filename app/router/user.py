from fastapi import FastAPI, Depends, Response, status, HTTPException, APIRouter
from typing import List
from .. import schemas, models
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags = ["User"],
)

@router.post('/add_users')
def create(request: schemas.UserBase):
    return user.create(request)

@router.get('/get_users',response_model = List[schemas.UserShow])
def get_all():
    return user.get_all()

@router.get('/get_users/{id}', status_code = status.HTTP_200_OK, response_model = schemas.UserShow)
def get_user(id:str, response:Response):
    return user.get_user(id)

@router.patch('/update_users/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(request: schemas.UserShow):
    return user.update(request)

@router.delete('/delete_users/{id}', status_code=status.HTTP_200_OK)
def delete(id: str):
    return user.delete(id)

@router.post("/send_invitation")
def send_invite():
    recipient_emails = ["pooja@aviato.consulting", "shraddha@aviato.consulting"]
    user.send_invitation(recipient_emails)
    return {"detail": "Invitation sent"}