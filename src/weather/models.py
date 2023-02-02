from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

from database import metadata

Base = declarative_base(metadata=metadata)


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    temperatures = Column(Integer, nullable=False)
    atmospheric_pressure = Column(Integer, nullable=False)
    wind_speed = Column(Integer, nullable=False)

    class Config:
        orm_mode = True


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    weather_id = Column(Integer, ForeignKey("weather.id"))

    class Config:
        orm_mode = True
