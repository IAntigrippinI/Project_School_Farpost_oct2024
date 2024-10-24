from sqlalchemy import select
from src.repositories.base import BaseRepository
from src.models.users import UsersOrm
from src.schemas.auth import User


class UsersRepository(BaseRepository):
    model = UsersOrm

    async def get_full_user(self, **filter_by) -> User:
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        model = result.scalars().one()
        return User.model_validate(model, from_attributes=True)
