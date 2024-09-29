import os
import json
import time
from confluent_kafka import Producer

# Sample JSON data
sample_json = {
    "event_id": "a1b2c3d4e5f6g7h8i9j0",
    "event_type": "splitpay",
    "timestamp": "2024-09-03T12:34:56Z",
    "data": {
        "user": "suraj",
        "location": "delhi",
        "amount": 250,
        "cash": "rupees"
    },
    "metadata": {
        "source": "simpl",
    }
}

# Delivery report function
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Function to produce events to Kafka
def produce_event_kafka():
    producer = Producer({'bootstrap.servers': 'kafka:9092'})  # Docker service name
    kafka_data = json.dumps(sample_json)  # Serialize to JSON string
    print('Serialized data to json')
    try:
        producer.produce('topic_splitpay', key=None, value=kafka_data, callback=delivery_report)
        producer.flush()
        print('Data published to Kafka')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    while True:
        produce_event_kafka()
        time.sleep(5)  # Wait for 5 seconds before sending the next message
