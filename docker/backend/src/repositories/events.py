from datetime import datetime, timedelta
from sqlalchemy import select, func
from src.repositories.base import BaseRepository
from src.models.events import EventsOrm
from src.schemas.events import Events


class EventsRepository(BaseRepository):
    model = EventsOrm
    schema = Events

    async def get_by_filter_pagin(
        self, limit, offset, category, date, price_from, price_to
    ):
        query = select(self.model)
        if category:
            query = query.filter(
                func.lower(EventsOrm.category).contains(category.lower())
            )
        if date:
            query = query.filter(date < date)
        if price_from:
            query = query.filter(price_from > price_from)

        if price_to:
            query = query.filter(price_to < price_to)

        query = query.limit(limit).offset(offset)
        result = await self.session.execute(query)
        model = result.scalars().all()
        return model
