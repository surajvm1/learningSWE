from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.weather_schema import WeatherData, WeatherResponse
from app.services.redis_service import set_weather, get_latest_weather, delete_latest_weather
from app.services.postgres_service import fetch_weather_from_postgres, add_weather_to_postgres, \
    update_weather_in_postgres, delete_weather_from_postgres
from app.services.mongodb_service import fetch_weather_from_mongodb, add_weather_to_mongodb, \
    update_weather_in_mongodb, delete_weather_from_mongodb
from app.db import get_db
import asyncio

router = APIRouter()

@router.get("/getWeather/{location}", response_model=WeatherResponse)
async def get_weather(location: str, db: Session = Depends(get_db)):
    cache = get_latest_weather(location)
    if cache:
        return cache

    weather = fetch_weather_from_postgres(db, location)
    if weather:
        set_weather(weather.location, weather.temperature)
        response_data = {
            "location": weather.location,
            "temperature": weather.temperature,
            "timestamp": weather.timestamp
        }
        return response_data

    weather = await fetch_weather_from_mongodb(location)
    if weather:
        set_weather(weather["location"], weather["temperature"])
        response_data = {
            "location": weather["location"],
            "temperature": weather["temperature"],
            "timestamp": weather["timestamp"]
        }
        return response_data

    raise HTTPException(status_code=404, detail="Weather data not found")

@router.post("/sendWeather")
async def send_weather(weather: WeatherData, db: Session = Depends(get_db)):
    await asyncio.gather(
        add_weather_to_postgres(db, weather),
        add_weather_to_mongodb(weather)
    )
    set_weather(weather.location, weather.temperature)
    response_data = {
        "message": "Weather data added successfully"
    }
    return response_data

@router.put("/updateWeather/{location}")
async def update_weather(location: str, weather: WeatherData, db: Session = Depends(get_db)):
    await asyncio.gather(
        update_weather_in_postgres(db, location, weather),
        update_weather_in_mongodb(location, weather)
    )
    set_weather(location, weather.temperature)
    response_data = {
        "message": "Weather data updated successfully"
    }
    return response_data

@router.delete("/deleteWeather/{location}")
async def delete_weather(location: str, db: Session = Depends(get_db)):
    await asyncio.gather(
        delete_weather_from_postgres(db, location),
        delete_weather_from_mongodb(location)
    )
    delete_latest_weather(location)
    response_data = {
        "message": "Weather data deleted successfully"
    }
    return response_data
