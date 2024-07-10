from pydantic import BaseModel, EmailStr
from typing import Optional, Dict
from datetime import date

class UserBase(BaseModel):
    company_name: Optional[str] = None
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    mobile_number: Optional[str] = None
    hashtag: Optional[str] = None
    dob: Optional[date] = None

    class Config:
        extra = "allow"

class UserShow(UserBase):
    id: str
    class Config:
        orm_mode = True