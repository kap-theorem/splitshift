from pydantic import BaseModel, Field

from models.user import User
from models.event import Event

class Space(BaseModel):
    id: int
    name: str
    description: str
    users: list[User]
    spaces: list['Space']
    events: list[Event]
