from kafka import KafkaConsumer
import json

def consume_topic_a():
    consumer = KafkaConsumer(
        'topic_a',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )

    for message in consumer:
        with open('topic_a_data.json', 'a') as f:
            json.dump(message.value, f)
            f.write('\n')  # Write each message on a new line

def consume_topic_b():
    consumer = KafkaConsumer(
        'dbserver1.public.weather',  # Topic created by Debezium
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )

    for message in consumer:
        with open('topic_b_data.json', 'a') as f:
            json.dump(message.value, f)
            f.write('\n')  # Write each message on a new line

if __name__ == "__main__":
    consume_topic_a()
    consume_topic_b()
