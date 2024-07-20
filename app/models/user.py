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


user = User(name='kek', id=1, age=10)
