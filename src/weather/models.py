from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

from database import metadata

Base = declarative_base(metadata=metadata)

city_weather_table = Table(
    "city_weather_table",
    Base.metadata,
    Column("city_id", ForeignKey("city.id"), primary_key=True),
    Column("weather_id", ForeignKey("weather.id"), primary_key=True),
)


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    temperatures = Column(Integer, nullable=False)
    atmospheric_pressure = Column(Integer, nullable=False)
    wind_speed = Column(Integer, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    class Config:
        orm_mode = True


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    city_id = Column(Integer, unique=True, nullable=False)
    weather = relationship(
        Weather, secondary=city_weather_table, backref="cities", lazy=True
    )

    def __repr__(self):
        return f"<City: {self.name}>"
