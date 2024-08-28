from confluent_kafka import Producer
from kafka import KafkaProducer
import json
# Create a Kafka producer - Confluent
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
