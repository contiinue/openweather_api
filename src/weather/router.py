from fastapi import APIRouter, status, Response
from .service import check_city_name

router = APIRouter(prefix="/weather")


@router.post("/{city}/")
async def add_city(city, response: Response):
    response_city: bool = await check_city_name(city)
    if response_city:
        response.status_code = status.HTTP_201_CREATED
        return {"message": "City added"}
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "invalid name city"}
