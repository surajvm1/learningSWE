from pydantic import BaseModel
from datetime import datetime

class WeatherData(BaseModel):
    user: str
    location: str
    temperature: int
    timestamp: datetime = datetime.utcnow()

class WeatherResponse(BaseModel):
    location: str
    temperature: int
    timestamp: datetime

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat(timespec='seconds') if isinstance(v, datetime) else v,
        }
