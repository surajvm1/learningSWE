from datetime import datetime
from app.schemas.weather_schema import WeatherData
from app.config import settings
import motor.motor_asyncio

MONGO_DATABASE_URL = f"mongodb://{settings.MONGO_INITDB_ROOT_USERNAME}:{settings.MONGO_INITDB_ROOT_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/{settings.MONGO_DB}"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DATABASE_URL)
db = client.weatherdb


async def fetch_weather_from_mongodb(location: str):
    document = await db.weather.find({"location": location}).sort("timestamp", -1).to_list(length=1)
    return document[0] if document else None


async def add_weather_to_mongodb(weather: WeatherData):
    document = weather.dict()
    document['timestamp'] = datetime.utcnow()
    result = await db.weather.insert_one(document)
    return document


async def update_weather_in_mongodb(location: str, weather: WeatherData):
    document = weather.dict()
    document['timestamp'] = datetime.utcnow()

    result = await db.weather.update_one(
        {"location": location},
        {"$set": document},
        sort=[("timestamp", -1)]
    )
    return document


async def delete_weather_from_mongodb(location: str):
    result = await db.weather.delete_one(
        {"location": location},
        sort=[("timestamp", -1)]
    )
    return result.deleted_count
