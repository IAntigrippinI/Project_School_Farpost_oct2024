from sqlalchemy import insert

from src.repositories.base import BaseRepository
from src.models.userStory import UserStoryOrm
from src.schemas.userStory import UserStoryAdd


class UserStoryRepository(BaseRepository):

    model = UserStoryOrm

    async def add_active(self, data: UserStoryAdd):
        stmt = insert(self.model).values(**data.model_dump())
        await self.session.execute(stmt)
        return "OK"
