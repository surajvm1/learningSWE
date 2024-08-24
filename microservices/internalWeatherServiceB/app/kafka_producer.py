from confluent_kafka import Producer
from kafka import KafkaProducer
import json
# Create a Kafka producer - Confluent
# def create_kafka_producer():
#     producer = Producer({'bootstrap.servers': 'kafka:9092'})  # Use the service name in Docker Compose
#     return producer

# Create a Kafka producer - Native
def create_kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',  # Use the service name in Docker Compose
        value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON
    )
    return producer
