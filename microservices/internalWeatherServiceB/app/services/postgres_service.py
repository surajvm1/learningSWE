from sqlalchemy.orm import Session
from datetime import datetime
from app.models.weather import Weather
from app.schemas.weather_schema import WeatherData

async def fetch_weather_from_postgres(db: Session, location: str):
    return db.query(Weather).filter(Weather.location == location).order_by(Weather.timestamp.desc()).first()

async def add_weather_to_postgres(db: Session, weather: WeatherData):
    weather_data = weather.dict()
    weather_data['timestamp'] = datetime.utcnow()
    db_weather = Weather(**weather_data)
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather

async def update_weather_in_postgres(db: Session, location: str, weather: WeatherData):
    db_weather = db.query(Weather).filter(Weather.location == location).order_by(Weather.timestamp.desc()).first()
    if db_weather:
        weather_data = weather.dict()
        weather_data['timestamp'] = datetime.utcnow()
        for key, value in weather_data.items():
            setattr(db_weather, key, value)
        db.commit()
        db.refresh(db_weather)
    return db_weather

async def delete_weather_from_postgres(db: Session, location: str):
    db_weather = db.query(Weather).filter(Weather.location == location).order_by(Weather.timestamp.desc()).first()
    if db_weather:
        db.delete(db_weather)
        db.commit()
    return db_weather
