from fastapi import FastAPI
from weather import routers as weather_router


app = FastAPI()
app.include_router(weather_router.router)

