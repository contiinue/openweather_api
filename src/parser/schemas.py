from pydantic import BaseModel


class WeatherResponse(BaseModel):
    temperatures: int
    atmospheric_pressure: int
    wind_speed: int
