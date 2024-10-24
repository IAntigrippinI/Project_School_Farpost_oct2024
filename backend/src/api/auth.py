import sqlalchemy
import asyncpg
from fastapi import APIRouter, Response, HTTPException
from src.schemas.auth import UserReqAdd, UserAdd
from src.services.auth import AuthService
from src.database import async_session_maker
from src.repositories.users import UsersRepository


router = APIRouter(prefix="/auth", tags=["Аутентификация"])


@router.post("/register")
async def register_user(data: UserReqAdd, responce: Response):
    try:
        hashed_pass = AuthService().hash_password(data.password)
        async with async_session_maker() as session:
            await UsersRepository(session=session).add(
                UserAdd(phone=data.phone, hashed_password=hashed_pass)
            )
            await session.commit()
        user = await UsersRepository(session=session).get_full_user(phone=data.phone)

        access_token = AuthService().create_access_token({"user_id": user.id})
        responce.set_cookie("access_token", access_token)
        return {"status": "OK"}
    except sqlalchemy.exc.IntegrityError as e:

        return {"status": "error", "message": "phone is register"}


@router.post("/login")
async def login_user(data: UserReqAdd, responce: Response):
    async with async_session_maker() as session:
        user = await UsersRepository(session=session).get_full_user(phone=data.phone)
        if not user:
            raise HTTPException(
                status_code=401, detail="Такого пользователя не существует"
            )
        if not AuthService().verify_password(data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Пароль неверный")
        access_token = AuthService().create_access_token({"user_id": user.id})
        responce.set_cookie("access_token", access_token)
        return {"token": access_token}
