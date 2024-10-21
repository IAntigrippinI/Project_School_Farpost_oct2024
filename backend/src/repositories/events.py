from src.repositories.base import BaseRepository
from src.models.events import EventsOrm


class EventsRepository(BaseRepository):
    model = EventsOrm
