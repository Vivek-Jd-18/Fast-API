from fastapi import FastAPI, Depends, Response, status, HTTPException, APIRouter
from typing import List
from .. import schemas
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags = ["User"],
)


"""
Create a new user.

Args:
    request (schemas.UserBase): The user data to be created.

Returns:
    The created user.

Raises:
    None.
"""
@router.post('/add_users')
def create(request: schemas.UserBase):
    return user.create(request)


"""
Get all users.

This function retrieves all users from the database and returns them as a list of `UserShow` objects.

Returns:
    List[schemas.UserShow]: A list of `UserShow` objects representing all the users in the database.
"""
@router.get('/get_users',response_model = List[schemas.UserShow])
def get_all():
    return user.get_all()


"""
Get a specific user by their ID.

Args:
    id (str): The ID of the user to retrieve.
    response (Response): The response object.

Returns:
    The user with the specified ID.
"""
@router.get('/get_users/{id}', status_code = status.HTTP_200_OK, response_model = schemas.UserShow)
def get_user(id:str, response:Response):
    return user.get_user(id)


"""
Updates a user in the 'users' collection based on the provided request.

Parameters:
    request (schemas.UserShow): The request object containing the updated user data.

Returns:
    dict: A dictionary containing the updated user data.

Raises:
    HTTPException: If the user with the specified ID is not found.
"""
@router.patch('/update_users/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(request: schemas.UserShow):
    return user.update(request)


"""
Deletes a user from the 'users' collection by their ID.

Args:
    id (str): The ID of the user to delete.

Returns:
    dict: A dictionary containing the message "deleted!" if the user was successfully deleted.

Raises:
    HTTPException: If the user with the specified ID is not found.
"""
@router.delete('/delete_users/{id}', status_code=status.HTTP_200_OK)
def delete(id: str):
    return user.delete(id)


"""
Sends an invitation email to the specified recipients.

This function sends an invitation email to the recipients specified in the `recipient_emails` list.
The email is sent using the `user.send_invitation` function, which takes a list of email addresses as input.

Parameters:
    None

Returns:
    A dictionary containing a single key-value pair, where the key is "detail" and the value is the string "Invitation sent".

Raises:
    None
"""
@router.post("/send_invitation")
def send_invite():
    recipient_emails = ["pooja@aviato.consulting", "shraddha@aviato.consulting"]
    user.send_invitation(recipient_emails)
    return {"detail": "Invitation sent"}