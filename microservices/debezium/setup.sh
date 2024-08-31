## Wait for Debezium to start
#sleep 10
#
## Create the PostgreSQL connector
#curl -X POST -H "Content-Type: application/json" \
#--data @/debezium/connectors/postgres_connector.json \
#http://debezium:8083/connectors
################################################################################################################
## Wait for Debezium to be healthy
#until curl -s http://localhost:8083/; do
#  echo "Waiting for Debezium to be ready..."
#  sleep 5
#done
#
## Create the PostgreSQL connector
#curl -X POST -H "Content-Type: application/json" \
#--data @/kafka/config/debezium_connector_config.json http://localhost:8083/connectors
################################################################################################################

#!/bin/bash
# Define the Kafka Connect URL
#CONNECT_URL="http://localhost:8083/connectors"
#echo "Waiting for Kafka Connect to be ready..."
#echo "Sleep mode for some time to ensure container is up before we check"
#sleep 15
## Check if Kafka Connect is ready
#while [[ $(curl -s -o /dev/null -w ''%{http_code}'' http://localhost:8083/connectors) != 200 ]]; do
#    echo "Kafka Connect is not ready yet. Waiting..."
#    sleep 5
#done
#echo "Kafka Connect is ready. Registering the connector."
## Register the Debezium connector using the variable
#curl -X POST -H "Content-Type: application/json" --data @/kafka/config/debezium_connector_config.json http://localhost:8083/connectors
#echo "Connector registered successfully."


###############################################################################################################
#
#/docker-entrypoint.sh start &
#
#echo "Waiting for Kafka Connect to be ready..."
#echo "Sleep mode for some time to ensure the container is up before we check"
#sleep 3
#response=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8083/connectors)
#user=$(whoami)
#echo "The current user is: $user"
#
#while [[ $response -ne 200 ]]; do
#    echo "Kafka Connect is not ready yet. Waiting... (Status: $response)"
#    sleep 3
#    response=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:8083/connectors)
#done
#echo "Kafka Connect is ready. Registering the connector."
#
#wait

################################################################
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

