from fastapi import APIRouter, Request
from src.database import async_session_maker
from src.repositories.events import EventsRepository
from src.schemas.events import EventsAdd


router = APIRouter(prefix="/events", tags=["Ивенты"])


@router.get("")
async def get_events(request: Request):
    access_token = request.cookies.get("access_token", None)
    async with async_session_maker() as session:
        res = await EventsRepository(session=session).get_all()
    return res


@router.post("")
async def add_event(data: EventsAdd):
    print(str(data.date))
    import datetime

    print(datetime.datetime.now())
    async with async_session_maker() as session:
        res = await EventsRepository(session).add(data)
        await session.commit()
    return res
