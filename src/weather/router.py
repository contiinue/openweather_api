from fastapi import APIRouter, Depends, Response, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from database import get_async_session

from .get_weather import add_city_to_model, check_city_name
from .models import City, Weather
from .schemas import CityStats

router = APIRouter(prefix="")


@router.post("/weather/{city}")
async def add_city(
    city, response: Response, db: AsyncSession = Depends(get_async_session)
):
    """Add the city to the database data if the city was tested by name."""
    response_city: int | None = await check_city_name(city)
    if response_city is not None:
        return await add_city_to_model(city, response_city, db, response)
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "invalid name city"}


@router.get("/last_weather/")
async def get_last_weather(search: str, db: AsyncSession = Depends(get_async_session)):
    """Getting cities(Filtered by name) with last Weather by time."""
    sub_q = aliased(
        select(City.name, func.max(Weather.time_created).label("time"))
        .where(City.name.like(f"{search.lower()}%"))
        .group_by(City.name)
        .subquery()
    )
    query = select(sub_q, Weather).join(Weather, sub_q.c.time == Weather.time_created)
    result = await db.execute(query)
    return result.all()


@router.get("/city_stats/")
async def get_city_stats(
    params: CityStats = Depends(),
    db: AsyncSession = Depends(get_async_session),
):
    """Getting all weather of city by filter time."""
    sub_q = select(func.avg(Weather.temperatures).label("average")).subquery()
    query = (
        select(City, Weather, sub_q)
        .where(City.name == params.search.lower())
        .filter(Weather.time_created.between(params.date_start, params.date_end))
    )
    result = await db.execute(query)
    return result.all()
