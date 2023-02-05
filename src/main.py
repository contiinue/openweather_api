from fastapi import FastAPI

from weather import router as weather_router

app = FastAPI()
app.include_router(weather_router.router)
