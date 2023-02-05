import datetime

from pydantic import BaseModel


class CityModel(BaseModel):
    id: int
    name: str
    city_id: int


class WeatherModel(BaseModel):
    id: int
    wind_speed: int
    temperatures: int
    atmospheric_pressure: int
    time_created: datetime.datetime


class CityStats(BaseModel):
    search: str
    date_start: datetime.datetime | None
    date_end: datetime.datetime | None


class CityStatsResponse(BaseModel):
    City: CityModel
    Weather: WeatherModel
    average: int

    class Config:
        orm_mode = True
