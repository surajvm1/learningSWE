from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.weather_schema import WeatherData, WeatherResponse
from app.services.redis_service import set_weather, get_latest_weather, delete_latest_weather
from app.services.postgres_service import fetch_weather_from_postgres, add_weather_to_postgres, \
    update_weather_in_postgres, delete_weather_from_postgres
from app.services.mongodb_service import fetch_weather_from_mongodb, add_weather_to_mongodb, update_weather_in_mongodb, \
    delete_weather_from_mongodb
from app.db import get_db
import asyncio
from app.db import init_db
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

if os.getenv("DOCKER_COMPOSE_MODE", "None") == 'True':
    init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def server_health_check():
    return {"Status": "Server healthy!"}

@app.get("/api/getWeather/{location}", response_model=WeatherResponse)
async def get_weather(location: str, db: Session = Depends(get_db)):
    cache = get_latest_weather(location)
    if cache:
        return cache

    weather = fetch_weather_from_postgres(db, location)
    if weather:
        set_weather(weather.location, weather.temperature)
        return {"location": weather.location, "temperature": weather.temperature, "timestamp": weather.timestamp}

    weather = await fetch_weather_from_mongodb(location)
    if weather:
        set_weather(weather["location"], weather["temperature"])
        return {"location": weather["location"], "temperature": weather["temperature"], "timestamp": weather["timestamp"]}

    raise HTTPException(status_code=404, detail="Weather data not found")

@app.post("/api/sendWeather")
async def send_weather(weather: WeatherData, db: Session = Depends(get_db)):
    await asyncio.gather(
        add_weather_to_postgres(db, weather),
        add_weather_to_mongodb(weather)
    )
    set_weather(weather.location, weather.temperature)
    return {"message": "Weather data added successfully"}

@app.put("/api/updateWeather/{location}")
async def update_weather(location: str, weather: WeatherData, db: Session = Depends(get_db)):
    await asyncio.gather(
        update_weather_in_postgres(db, location, weather),
        update_weather_in_mongodb(location, weather)
    )
    set_weather(location, weather.temperature)
    return {"message": "Weather data updated successfully"}

@app.delete("/api/deleteWeather/{location}")
async def delete_weather(location: str, db: Session = Depends(get_db)):
    await asyncio.gather(
        delete_weather_from_postgres(db, location),
        delete_weather_from_mongodb(location)
    )
    delete_latest_weather(location)
    return {"message": "Weather data deleted successfully"}
