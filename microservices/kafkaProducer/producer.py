from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import os
from confluent_kafka import Producer
from kafka import KafkaProducer
import json

app = FastAPI()

def create_kafka_producer():
    producer = Producer({'bootstrap.servers': 'kafka:9092'})  # Use the service name in Docker Compose
    # producer = Producer({'bootstrap.servers': 'localhost:29092'}) # Use the host port for local testing
    return producer

# Create a Kafka producer - Native
# def create_kafka_producer():
#     producer = KafkaProducer(
#         # bootstrap_servers='kafka:9092',  # Use the service name in Docker Compose
#         bootstrap_servers='localhost:29092',  # Use the host port for local testing
#         value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON
#     )
#     return producer
producer = create_kafka_producer()

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

class WeatherDataPayload(BaseModel):
    timestamp: str
    temperature: int
    location: str

# Create the POST endpoint
@app.post("/sendKafka")
async def publish_to_kafka(weather_data_payload: WeatherDataPayload):
    try:
        # Convert the Pydantic model to a JSON string
        weather_data_json = weather_data_payload.json()
        producer.produce('topic_a', key=None, value=weather_data_json, callback=delivery_report)
        producer.flush()
    except Exception as e:
        print(e)
