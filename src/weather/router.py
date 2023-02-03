from fastapi import APIRouter, Depends, Response, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from database import get_async_session

from .models import City, Weather
from .service import add_city_to_model, check_city_name

router = APIRouter(prefix="")


@router.post("/weather/{city}")
async def add_city(
    city, response: Response, session: AsyncSession = Depends(get_async_session)
):
    response_city: int | None = await check_city_name(city)
    if response_city is not None:
        return await add_city_to_model(city, response_city, session, response)
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "invalid name city"}


@router.get("/last_weather/")
async def get_last_weather(search: str, db: AsyncSession = Depends(get_async_session)):
    sub_q = aliased(
        select(City.name, func.max(Weather.time_created).label("time"))
        .where(City.name.like(f"{search}%"))
        .group_by(City.name)
        .subquery()
    )
    query = select(sub_q, Weather).join(Weather, sub_q.c.time == Weather.time_created)
    result = await db.execute(query)
    return result.all()
