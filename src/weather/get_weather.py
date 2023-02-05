import aiohttp
from fastapi import status
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from websockets.http11 import Response

from config import settings

from .models import City
from .weather_config import PATH_TO_CHECK_CITY


async def check_city_name(city_name: str) -> str | None:
    """Check city name and return his id in openweather."""
    async with aiohttp.ClientSession() as session:
        url = PATH_TO_CHECK_CITY.format(
            city=city_name, key=settings.OPEN_WEATHER_API_KEY
        )
        async with session.get(url=url) as response:
            response = await response.json()
            try:
                return response["list"][0]["id"]
            except (KeyError, IndexError):
                return None


async def add_city_to_model(
    city_name: str, city_id, session: AsyncSession, response: Response
) -> dict:
    """Save city to the database."""
    try:
        stmt = insert(City).values(name=city_name.lower(), city_id=city_id)
        await session.execute(stmt)
        await session.commit()
        response.status_code = status.HTTP_201_CREATED
        return {"message": "City added"}
    except IntegrityError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "City apply"}
