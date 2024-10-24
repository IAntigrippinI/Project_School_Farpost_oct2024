from src.repositories.base import BaseRepository
from src.models.savedEvents import SavedEventsOrm
from src.schemas.savedEvents import SavedEvents


class SavedEventsRepositopry(BaseRepository):
    model = SavedEventsOrm
    schema = SavedEvents
