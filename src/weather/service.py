import aiohttp
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from websockets.http11 import Response

from fastapi import status
from config import settings
from .models import City
from .weather_config import PATH_TO_CHECK_CITY


async def check_city_name(city_name: str) -> bool:
    async with aiohttp.ClientSession() as session:
        url = PATH_TO_CHECK_CITY.format(
            city=city_name, limit=5, key=settings.OPEN_WEATHER_API_KEY
        )
        async with session.get(url=url) as response:
            response = await response.json()
            return any(response) or False


async def add_city_to_model(
    city_name: str, session: AsyncSession, response: Response
) -> dict:
    try:
        stmt = insert(City).values(name=city_name)
        await session.execute(stmt)
        await session.commit()
        response.status_code = status.HTTP_201_CREATED
        return {"message": "City added"}
    except IntegrityError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "City apply"}
