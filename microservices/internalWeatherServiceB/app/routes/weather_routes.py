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
from app.kafka_producer import create_kafka_producer
import asyncio
import json

router = APIRouter()
producer = create_kafka_producer()
@router.get("/getWeather/{location}", response_model=WeatherResponse)
async def get_weather(location: str, db: Session = Depends(get_db)):

    # producer.send('topic_a', {
    #     "location": 'hello',
    #     "temperature": 300,
    #     "timestamp": 'hohoho'
    # })
    # producer.flush()

    def delivery_report(err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    try:
        producer.produce('topic_a', key=None, value=json.dumps({
            "location": 'hello',
            "temperature": 300,
            "timestamp": 'hohoho'
        }),
        callback = delivery_report
        )
        producer.flush()
    except Exception as e:
        print(e)

    cache = get_latest_weather(location)
    if cache:
        return cache

    weather = await fetch_weather_from_postgres(db, location)
    if weather:
        set_weather(weather.location, weather.temperature) ## caching in redis
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

    # fallback mechanism
    weather = get_weather_data_ext_service(location)
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


"""
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer

def create_kafka_topic(topic_name, num_partitions=1, replication_factor=1):
    admin_client = AdminClient({'bootstrap.servers': 'kafka:9092'})
    
    # Check if topic already exists
    topic_metadata = admin_client.list_topics(timeout=10)
    if topic_name not in topic_metadata.topics:
        topic = NewTopic(topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
        admin_client.create_topics([topic])
        print(f"Topic '{topic_name}' created.")

def create_kafka_producer():
    producer = Producer({'bootstrap.servers': 'kafka:9092'})
    return producer

# Create the topic if it doesn't exist
create_kafka_topic('topic_a')

# Produce a message to the topic
producer = create_kafka_producer()
producer.produce('topic_a', key=None, value='{"location": "hello", "temperature": 300, "timestamp": "hohoho"}')
producer.flush()

-----------

from confluent_kafka import Producer, KafkaError

def create_kafka_producer():
    producer = Producer({'bootstrap.servers': 'kafka:9092'})
    return producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

producer = create_kafka_producer()
try:
    producer.produce('topic_a', key=None, value='{"location": "hello", "temperature": 300, "timestamp": "hohoho"}', callback=delivery_report)
    producer.flush()
except KafkaError as e:
    if e.args[0].code() == KafkaError.UNKNOWN_TOPIC_OR_PART:
        # Handle topic creation if needed
        create_kafka_topic('topic_a')

"""