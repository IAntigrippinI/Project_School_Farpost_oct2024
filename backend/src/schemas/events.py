from pydantic import BaseModel, Field
from datetime import datetime


class EventsGet(BaseModel):
    title: str | None = Field(None)
    category: str | None = Field(None)


class EventsAdd(BaseModel):
    title: str
    poster_url: str
    date: datetime
    post_date: datetime
    category: str
    price_from: int
    price_to: int
    creater_id: int
    likes: int
    dislikes: int
    views: int


class Events(EventsAdd):
    id: int
