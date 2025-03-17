from pydantic import BaseModel

from models.event import Event
from models.user import User


class Space(BaseModel):
    id: int
    name: str
    description: str
    users: list[User]
    spaces: list["Space"]
    events: list[Event]
