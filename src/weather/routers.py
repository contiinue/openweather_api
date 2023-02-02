from fastapi import APIRouter

router = APIRouter(prefix='/weather')


@router.post("/{city}")
async def add_city(city):
    
    return {"message": city}
