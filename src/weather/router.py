from fastapi import APIRouter, status, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from .service import check_city_name, add_city_to_model

router = APIRouter(prefix="/weather")


@router.post("/{city}/")
async def add_city(
    city, response: Response, session: AsyncSession = Depends(get_async_session)
):
    response_city: bool = await check_city_name(city)
    if response_city:
        return await add_city_to_model(city, session, response)
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "invalid name city"}
