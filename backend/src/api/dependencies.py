from typing import Annotated
from fastapi import Depends, Request, HTTPException
from src.services.auth import AuthService


async def get_token(request: Request):
    access_token = request.cookies.get(
        "access_token", None
    )  # поиск по словарю делается с исп .get(key, if not key)
    if not access_token:
        raise HTTPException(status_code=401, detail="Пользователь не аутентифицирован")
    return access_token


async def get_user_id(token: str = Depends(get_token)):
    if token:
        data = AuthService().decode_token(token)
    return data["user_id"]


UserIdDep = Annotated[int, Depends(get_user_id)]
