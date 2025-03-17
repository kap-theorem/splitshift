from pydantic import BaseModel, Field
from typing import Annotated

class User(BaseModel):
    id: int
    name: str
    age: Annotated[int, Field(gt=0 , lt=150)]
    email: str
    password: str
