from pydantic import BaseModel, Field

from models.user import User

class Event(BaseModel):
    id: int
    name: str
    description: str
    space_id: int
    users: list[User]