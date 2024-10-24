from src.repositories.base import BaseRepository
from src.models.userEvents import UserEventsOrm
from src.schemas.savedEvents import SavedEvents


class UserEventsRepository(BaseRepository):
    model = UserEventsOrm
    schema = SavedEvents
