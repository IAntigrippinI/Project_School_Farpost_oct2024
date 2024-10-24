from pydantic import BaseModel


class SavedEventsAdd(BaseModel):
    user_id: int
    event_id: int


class SavedEvents(SavedEventsAdd):
    id: int
