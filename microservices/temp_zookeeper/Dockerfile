# Use Ubuntu as the base image
FROM ubuntu:20.04

# Install Java and other necessary packages
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Download and extract Zookeeper
ENV ZOOKEEPER_VERSION 3.7.0
RUN wget https://downloads.apache.org/zookeeper/zookeeper-$ZOOKEEPER_VERSION/apache-zookeeper-$ZOOKEEPER_VERSION-bin.tar.gz \
    && tar -xzf apache-zookeeper-$ZOOKEEPER_VERSION-bin.tar.gz \
    && mv apache-zookeeper-$ZOOKEEPER_VERSION-bin /zookeeper

# Set working directory
WORKDIR /zookeeper

# Expose Zookeeper port
EXPOSE 2181

# Start Zookeeper
CMD ["bin/zkServer.sh", "start-foreground"]

#FROM ubuntu:22.04
#
#RUN apt-get update && \
#    apt-get install -y openjdk-11-jdk wget && \
#    wget https://downloads.apache.org/zookeeper/zookeeper-3.7.1/apache-zookeeper-3.7.1-bin.tar.gz && \
#    tar -xvf apache-zookeeper-3.7.1-bin.tar.gz && \
#    mv apache-zookeeper-3.7.1-bin /opt/zookeeper
#
#ENV ZOOKEEPER_HOME=/opt/zookeeper
#ENV PATH=$PATH:$ZOOKEEPER_HOME/bin
#
#CMD ["zkServer.sh", "start-foreground"]

