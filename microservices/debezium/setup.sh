##!/bin/bash
#
## Wait for Debezium to start
#sleep 10
#
## Create the PostgreSQL connector
#curl -X POST -H "Content-Type: application/json" \
#--data @/debezium/connectors/postgres_connector.json \
#http://debezium:8083/connectors

#!/bin/bash

# Wait for Debezium to be healthy
until curl -s http://localhost:8083/; do
  echo "Waiting for Debezium to be ready..."
  sleep 5
done

# Create the PostgreSQL connector
curl -X POST -H "Content-Type: application/json" \
--data @/kafka/config/debezium_connector_config.json http://localhost:8083/connectors