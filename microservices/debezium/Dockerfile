FROM quay.io/debezium/connect:latest

# Copy the initialization script
COPY setup.sh /setup.sh
COPY connectors/postgres_connector.json /kafka/config/debezium_connector_config.json

# Make the script executable
# RUN chmod +x /setup.sh

# Start Debezium and run the initialization script
CMD ["bash", "/setup.sh"]