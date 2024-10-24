from datetime import datetime
from fastapi import APIRouter
from src.schemas.savedEvents import SavedEventsAdd
from src.repositories.savedEvents import SavedEventsRepositopry
from src.repositories.userEvents import UserEventsRepository
from src.api.dependencies import UserIdDep
from src.database import async_session_maker
from src.repositories.userStory import UserStoryRepository
from src.schemas.userStory import UserStoryAdd

router = APIRouter(prefix="/userEvents", tags=["Взаимодейтсвие пользователей"])


@router.post("/{event_id}", description="Добавление мероприятия в избранное")
async def add_event_to_me(event_id: int, user_id: UserIdDep):
    async with async_session_maker() as session:
        await UserStoryRepository(session).add(
            UserStoryAdd(
                time=datetime.now(),
                user_id=user_id,
                event_id=event_id,
                action="Add to saved",
            )
        )
        await SavedEventsRepositopry(session).add(
            SavedEventsAdd(user_id=user_id, event_id=event_id)
        )
        await session.commit()


@router.get("", description="Получение избранных мероприятий")
async def get_saved_events(user_id: UserIdDep):
    async with async_session_maker() as session:
        user_events = await SavedEventsRepositopry(session).get_by_filter(
            user_id=user_id
        )

    return user_events


@router.post("/buy/{event_id}", description="Добавление мероприятия в купленное")
async def add_buy_event_to_me(event_id: int, user_id: UserIdDep):
    async with async_session_maker() as session:
        await UserStoryRepository(session).add(
            UserStoryAdd(
                time=datetime.now(),
                user_id=user_id,
                event_id=event_id,
                action="SuccessPurchase",
            )
        )
        await UserEventsRepository(session).add(
            SavedEventsAdd(user_id=user_id, event_id=event_id)
        )
        await session.commit()


@router.get("/my", description="ПОлучение купленных билетов")
async def get_bought_events(user_id: UserIdDep):
    async with async_session_maker() as session:
        user_events = await UserEventsRepository(session).get_by_filter(user_id=user_id)

    return user_events


@router.delete("/{event_id}", description="Удаление сохраненного мероприятия")
async def delete_event_from_saved(event_id: int, user_id: UserIdDep):
    async with async_session_maker() as session:
        await UserStoryRepository(session).add(
            UserStoryAdd(
                time=datetime.now(),
                user_id=user_id,
                event_id=event_id,
                action="Delete from saved",
            )
        )
        await SavedEventsRepositopry(session).delete(user_id=user_id, event_id=event_id)
        await session.commit()
    return "OK"


@router.delete("/buy/{event_id}", description="Удаление купленного мероприятия")
async def delete_event_from_buy(event_id: int, user_id: UserIdDep):
    async with async_session_maker() as session:
        await UserStoryRepository(session).add(
            UserStoryAdd(
                time=datetime.now(),
                user_id=user_id,
                event_id=event_id,
                action="Delete buy",
            )
        )
        await UserEventsRepository(session).delete(user_id=user_id, event_id=event_id)
        await session.commit()
    return "OK"
