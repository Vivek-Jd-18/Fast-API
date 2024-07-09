from sqlalchemy import Column, Integer, String, Date
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True, nullable=True)
    password = Column(String, nullable=True)
    mobile_number = Column(String, index=True, nullable=True)
    hashtag = Column(String, index=True, nullable=True)
    dob = Column(Date, nullable=True)