#!/bin/bash
/docker-entrypoint.sh start &
echo "Waiting for Kafka Connect to be ready..."
echo "Sleep mode for some time to ensure the container is up before we check"
sleep 5
user=$(whoami)
echo "The current user in debezium container is: $user"
response=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8083/connectors)
echo "Status code hitting URL to create Kafka connect: response"
while [[ $response -ne 200 ]]; do
    echo "Kafka Connect is not ready yet. Waiting... (Status: $response)"
    sleep 3
    response=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8083/connectors)
done
echo "Kafka Connect is ready. Registering the connector."
# Register the Debezium connector using the variable
curl -X POST -H "Content-Type: application/json" --data @/kafka/config/debezium_connector_config.json http://localhost:8083/connectors
echo "Connector registered successfully."
wait
