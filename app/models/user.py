from pydantic import BaseModel
from typing import Union, Optional


class User(BaseModel):
    name: str
    id: Optional[int] = None
    age: int


class IsAdultUser(BaseModel):
    name: str
    id: Union[int, None]
    age: int
    is_adult: Optional[bool] = None


class CreateUser(BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool


class UserLogin(BaseModel):
    login: str
    password: str


user = User(name='kek', id=1, age=10)

user_login = {
    "username": "user123",
    "password": "password123"
}

session_token_base = '1234'
