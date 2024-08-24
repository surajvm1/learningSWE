#!/bin/bash

# Wait for Debezium to start
sleep 10

# Create the PostgreSQL connector
curl -X POST -H "Content-Type: application/json" \
--data @/debezium/connectors/postgres_connector.json \
http://debezium:8083/connectors