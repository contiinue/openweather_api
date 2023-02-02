import aiohttp

from config import settings
from .weather_config import PATH_TO_CHECK_CITY


async def check_city_name(city_name: str) -> bool:
    async with aiohttp.ClientSession() as session:
        url = PATH_TO_CHECK_CITY.format(
            city=city_name, limit=5, key=settings.OPEN_WEATHER_API_KEY
        )
        async with session.get(url=url) as response:
            response = await response.json()
            return any(response) or False
