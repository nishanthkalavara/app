from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    pass

class Userid(UserBase):
    id: int 
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    name: str
    url: str
    caption: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    name: str
    url: str
    caption: str

    class Config:
        orm_mode = True