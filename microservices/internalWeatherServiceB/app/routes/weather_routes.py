from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.weather_schema import WeatherData, WeatherResponse
from app.services.redis_service import set_weather, get_latest_weather, delete_latest_weather
from app.services.postgres_service import fetch_weather_from_postgres, add_weather_to_postgres, \
    update_weather_in_postgres, delete_weather_from_postgres
from app.services.mongodb_service import fetch_weather_from_mongodb, add_weather_to_mongodb, \
    update_weather_in_mongodb, delete_weather_from_mongodb
from app.services.external_weather_service import get_weather_data_ext_service
from app.db import get_db
import asyncio
import json
import requests

router = APIRouter()

def send_data_kafka(payload):
    # Headers, if required (e.g., for content type, authorization, etc.)
    headers = {
        "Content-Type": "application/json",
    }
    kafka_producer_url = f'http://kafka_producer:8325/sendKafka'
    try:
        response = requests.post(kafka_producer_url, json=payload, headers=headers)
        response_status_code = response.status_code
        if response_status_code == 200:
            print("Data published to Kafka")
        else:
            print(f"Failed to post data. Status code: {response_status_code}")
    except Exception as e:
        print(f"An error occurred while posting data: {e}")

@router.get("/getWeather/{location}", response_model=WeatherResponse)
async def get_weather(location: str, db: Session = Depends(get_db)):

    cache = get_latest_weather(location)
    if cache:
        return cache

    payload = {
        "service": "internalService"
    }
    weather = await fetch_weather_from_postgres(db, location)
    if weather:
        set_weather(weather.location, weather.temperature) ## caching in redis
        response_data = {
            "location": weather.location,
            "temperature": weather.temperature,
            "timestamp": weather.timestamp
        }
        payload = {**payload, **response_data}
        send_data_kafka(payload)
        return response_data

    weather = await fetch_weather_from_mongodb(location)
    if weather:
        set_weather(weather["location"], weather["temperature"])
        response_data = {
            "location": weather["location"],
            "temperature": weather["temperature"],
            "timestamp": weather["timestamp"]
        }
        payload = {**payload, **response_data}
        send_data_kafka(payload)
        return response_data

    # fallback mechanism
    weather = get_weather_data_ext_service(location)
    if weather:
        set_weather(weather["location"], weather["temperature"])
        response_data = {
            "location": weather["location"],
            "temperature": weather["temperature"],
            "timestamp": weather["timestamp"]
        }
        payload = {**payload, **response_data}
        send_data_kafka(payload)
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
