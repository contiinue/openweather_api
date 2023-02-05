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


scrapy_settings = scrapy.settings.Settings(values={"LOG_LEVEL": "WARNING"})
processor = Processor(settings=scrapy_settings)


def get_session():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    with sessionmaker(engine)() as session:
        return session


class WeatherSpider(scrapy.Spider):
    name = "weather"
    base_url = "https://openweathermap.org/data/2.5/weather?id={city}&appid={key}"
    db = get_session()

    def start_requests(self):
        q = select(City)
        cities = self.db.execute(q).scalars().all()
        for city in cities:
            url = self.base_url.format(
                city=city.city_id, key=settings.OPEN_WEATHER_API_KEY
            )
            yield Request(url=url, cb_kwargs={"city": city})

    def parse(self, response, **kwargs):
        data = self._get_response_data(response.json())
        self._save_response_to_database(data, kwargs["city"])

    def _save_response_to_database(self, data: WeatherResponse, city: City) -> None:
        weather = Weather(**data.__dict__)
        city.weather.append(weather)
        self.db.add(city)
        self.db.add(weather)
        self.db.commit()

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
