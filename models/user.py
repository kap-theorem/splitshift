from typing import Annotated

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    age: Annotated[int, Field(gt=0, lt=150)]
    email: str
    password: str
