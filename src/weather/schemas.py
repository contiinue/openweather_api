from pydantic import BaseModel


class CitySchemas(BaseModel):
    id: int
    name: str
    city_id: int
    weather_id: int

    class Config:
        orm_mode = True
