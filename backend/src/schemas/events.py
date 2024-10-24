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


class EventByFitler(BaseModel):
    category: str


class EventsPATCH(BaseModel):
    title: str | None = None
    poster_url: str | None = None
    date: datetime | None = None
    post_date: datetime | None = None
    category: str | None = None
    price_from: int | None = None
    price_to: int | None = None
    creater_id: int | None = None
    likes: int | None = None
    dislikes: int | None = None
    views: int | None = None
