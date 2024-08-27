FROM ubuntu:20.04

# Install Java and necessary packages
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Debezium version
ENV DEBEZIUM_VERSION 1.9.7.Final
ENV KAFKA_VERSION 3.1.0
ENV DEBEZIUM_HOME /opt/debezium

# Download and extract Debezium
RUN wget https://downloads.jboss.org/debezium/releases/$DEBEZIUM_VERSION/debezium-connector-postgresql-$DEBEZIUM_VERSION-plugin.tar.gz \
    && mkdir -p $DEBEZIUM_HOME \
    && tar -xzf debezium-connector-postgresql-$DEBEZIUM_VERSION-plugin.tar.gz -C $DEBEZIUM_HOME \
    && rm debezium-connector-postgresql-$DEBEZIUM_VERSION-plugin.tar.gz

# Expose the necessary ports
EXPOSE 8083

# Copy the setup script and connector configuration
COPY setup.sh /setup.sh
COPY connectors/postgres_connector.json /connectors/postgres_connector.json

# Start Debezium
CMD ["bash", "/setup.sh"]

#FROM ubuntu:22.04
#
#RUN apt-get update && \
#    apt-get install -y openjdk-11-jdk wget && \
#    wget https://repo1.maven.org/maven2/io/debezium/debezium-server-dist/1.8.0.Final/debezium-server-dist-1.8.0.Final.tar.gz && \
#    tar -xvf debezium-server-dist-1.8.0.Final.tar.gz && \
#    mv debezium-server-dist-1.8.0.Final /opt/debezium
#
#ENV DEBEZIUM_HOME=/opt/debezium
#ENV PATH=$PATH:$DEBEZIUM_HOME/bin
#
#CMD ["debezium-server", "run"]
