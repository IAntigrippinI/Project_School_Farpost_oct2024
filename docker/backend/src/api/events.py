from datetime import datetime
from fastapi import APIRouter, Request, Query
from src.database import async_session_maker
from src.repositories.events import EventsRepository
from src.schemas.events import EventsAdd, EventByFitler


router = APIRouter(prefix="/events", tags=["Ивенты"])


@router.get("")
async def get_events(
    request: Request,
    category: str = Query(None),
    date: datetime = Query(None),
    price_from: int = Query(None),
    price_to: int = Query(None),
    page: int = Query(1),
    per_page: int = Query(15),
):
    access_token = request.cookies.get("access_token", None)
    async with async_session_maker() as session:
        res = await EventsRepository(session=session).get_by_filter_pagin(
            limit=per_page,
            offset=per_page * (page - 1),
            category=category,
            date=date,
            price_from=price_from,
            price_to=price_to,
        )
    return res


@router.get("/{id}")
async def get_by_id(id: int):
    async with async_session_maker() as session:
        return await EventsRepository(session).get_one_or_none(id=id)


@router.get("/get_rec/")
def what():
    print("ok")


@router.post("")
async def add_event(data: EventsAdd):
    print(str(data.date))
    import datetime

    print(datetime.datetime.now())
    async with async_session_maker() as session:
        res = await EventsRepository(session).add(data)
        await session.commit()
    return res
