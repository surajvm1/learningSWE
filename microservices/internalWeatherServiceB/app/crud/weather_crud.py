from sqlalchemy.orm import Session
from app.models.weather import Weather
from app.schemas.weather_schema import WeatherData

def get_weather(db: Session, location: str):
    return db.query(Weather).filter(Weather.location == location).first()

def create_weather(db: Session, weather: WeatherData):
    db_weather = Weather(**weather.dict())
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather

def update_weather(db: Session, location: str, weather: WeatherData):
    db_weather = db.query(Weather).filter(Weather.location == location).first()
    if db_weather:
        for key, value in weather.dict().items():
            setattr(db_weather, key, value)
        db.commit()
        db.refresh(db_weather)
    return db_weather

def delete_weather(db: Session, location: str):
    db_weather = db.query(Weather).filter(Weather.location == location).first()
    if db_weather:
        db.delete(db_weather)
        db.commit()
    return db_weather
