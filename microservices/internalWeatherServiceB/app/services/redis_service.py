import redis
from datetime import datetime
from app.config import settings

redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True
)

def set_weather(location: str, temperature: int):
    timestamp = datetime.utcnow().isoformat()
    key = f"{location}:{timestamp}"
    redis_client.set(key, temperature)

def get_latest_weather(location: str):
    keys = redis_client.keys(f"{location}:*")
    if not keys:
        return None

    latest_key = max(keys)
    return {
        "location": location,
        "temperature": int(redis_client.get(latest_key)),
        "timestamp": latest_key.split(":")[1]
    }

def delete_latest_weather(location: str):
    keys = redis_client.keys(f"{location}:*")
    if not keys:
        return 0

    latest_key = max(keys)
    return redis_client.delete(latest_key)
