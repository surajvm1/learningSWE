# Use Ubuntu as the base image
FROM ubuntu:20.04

# Install Java and other necessary packages
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Kafka version
ENV KAFKA_VERSION 3.1.0
ENV KAFKA_HOME /opt/kafka

# Download and extract Kafka
RUN wget https://downloads.apache.org/kafka/$KAFKA_VERSION/kafka_2.13-$KAFKA_VERSION.tgz \
    && tar -xzf kafka_2.13-$KAFKA_VERSION.tgz -C /opt/ \
    && rm kafka_2.13-$KAFKA_VERSION.tgz

# Set working directory
WORKDIR $KAFKA_HOME

# Expose Kafka ports
EXPOSE 9092

# Start Kafka
CMD ["bin/kafka-server-start.sh", "config/server.properties"]

#FROM ubuntu:22.04
#
#RUN apt-get update && \
#    apt-get install -y openjdk-11-jdk wget && \
#    wget https://downloads.apache.org/kafka/3.3.1/kafka_2.13-3.3.1.tgz && \
#    tar -xvf kafka_2.13-3.3.1.tgz && \
#    mv kafka_2.13-3.3.1 /opt/kafka
#
#ENV KAFKA_HOME=/opt/kafka
#ENV PATH=$PATH:$KAFKA_HOME/bin
#
#COPY server.properties $KAFKA_HOME/config/
#
#CMD ["kafka-server-start.sh", "/opt/kafka/config/server.properties"]
