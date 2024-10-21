from pydantic import BaseModel


class UserReqAdd(BaseModel):
    phone: str
    password: str


class UserAdd(BaseModel):
    phone: str
    hashed_password: str


class User(UserAdd):
    id: int
