import datetime

from pydantic import BaseModel


class CityModel(BaseModel):
    id: int
    name: str
    city_id: int

    class Config:
        orm_mode = True


class WeatherModel(BaseModel):
    id: int
    wind_speed: int
    temperatures: int
    atmospheric_pressure: int
    time_created: datetime.datetime

    class Config:
        orm_mode = True


class CityStats(BaseModel):
    search: str
    date_start: datetime.date | None
    date_end: datetime.date | None


class CityStatsResponse(BaseModel):
    City: CityModel
    Weather: WeatherModel
    average: int

    class Config:
        orm_mode = True


class LastWeatherResponse(BaseModel):
    name: str
    time: datetime.datetime
    Weather: WeatherModel

    class Config:
        orm_mode = True
