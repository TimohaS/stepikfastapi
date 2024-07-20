from pydantic import BaseModel
from typing import Optional


class Feeback(BaseModel):
    name: str
    message: Optional[str] = None


class FeedbackResponce(BaseModel):
    message: str
