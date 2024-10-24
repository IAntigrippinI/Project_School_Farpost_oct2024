from datetime import datetime
from pydantic import BaseModel


class UserStoryAdd(BaseModel):
    time: datetime
    user_id: int
    event_id: int
    action: str


class UserStory(UserStoryAdd):
    id: int
