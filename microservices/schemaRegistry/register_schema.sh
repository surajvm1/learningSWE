#!/bin/bash

# Schema for weather data
SCHEMA='{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "location": {"type": "string"},
    "temperature": {"type": "integer"},
    "timestamp": {"type": "string"}
  },
  "required": ["location", "temperature", "timestamp"]
}'

# Register the schema
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
    --data "{\"schema\": \"$SCHEMA\"}" \
    http://localhost:8081/subjects/topic_a-value/versions)

# Check if the registration was successful
if [ "$RESPONSE" -eq 200 ]; then
    echo "Schema registered successfully."
else
    echo "Failed to register schema. HTTP response code: $RESPONSE"
fi