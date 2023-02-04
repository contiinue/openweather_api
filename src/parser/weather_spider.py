from parser.schemas import WeatherResponse

import scrapy
from scrapy.http import Request
from scrapyscript import Job, Processor
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from config import settings
from weather.models import City, Weather


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}"
    f":{settings.POSTGRES_PORT}/{settings.POSTGRES_DATABASE}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(engine)()

processor = Processor(settings=None)


class WeatherSpider(scrapy.Spider):
    name = "weather"
    base_url = "https://openweathermap.org/data/2.5/weather?id={city}&appid={key}"

    def start_requests(self):
        q = select(City)
        cities = session.execute(q).scalars().all()
        for city in cities:
            url = self.base_url.format(
                city=city.city_id, key=settings.OPEN_WEATHER_API_KEY
            )
            yield Request(url=url, cb_kwargs={"city": city})

    def parse(self, response, **kwargs):
        data = self._get_response_data(response.json())
        self._save_response_to_database(data, kwargs["city"])

    @staticmethod
    def _save_response_to_database(data: WeatherResponse, city: City) -> None:
        weather = Weather(**data.__dict__)
        city.weather.append(weather)
        session.add(city)
        session.add(weather)
        session.commit()

    @staticmethod
    def _get_response_data(data) -> WeatherResponse:
        return WeatherResponse(
            wind_speed=data["wind"]["speed"],
            atmospheric_pressure=data["main"]["pressure"],
            temperatures=data["main"]["temp"],
        )


def start_spider():
    job = Job(WeatherSpider)
    processor.run(job)


if __name__ == "__main__":
    start_spider()
