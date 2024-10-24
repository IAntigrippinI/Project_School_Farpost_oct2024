from sqlalchemy import func, select, insert, update, delete
import sqlalchemy.ext
import sqlalchemy.ext.asyncio
from pydantic import BaseModel


class BaseRepository:
    model = None
    schema: BaseModel = None

    def __init__(self, session):
        self.session = session

    async def get_one_or_none(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        model = res.scalars().one_or_none()

        # return self.schema.model_validate(model, from_attributes=True)\
        return model

    async def get_all(self):
        stmt = select(self.model)
        model = await self.session.execute(stmt)
        return model.scalars().all()

    async def get_by_filter(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        model = await self.session.execute(stmt)
        return model.scalars().all()

    async def add(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        model = await self.session.execute(stmt)
        return model.scalars().one()

    async def get_with_pagination(self, limit, offset, **filter_by):
        query = select(self.model).filter_by(**filter_by).limit(limit).offset(offset)
        print(query.compile(compile_kwargs={"literal_binds": True}))
        res = await self.session.execute(query)
        model = res.scalars().all()
