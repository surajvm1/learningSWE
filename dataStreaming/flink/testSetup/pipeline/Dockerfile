## Multi stage build - Added Dockerfile just for reference. Not using it currently.
#FROM --platform=linux/amd64 maven:3.6.3 AS maven
#COPY . /usr/app
#WORKDIR /usr/app
#ARG APP_ENV
#RUN mvn clean package -DskipTests -P ${APP_ENV}
#
#FROM --platform=linux/amd64 flink:1.17.1-java11
#ARG JAR_FILE=target/pi3flinkpipeline-1.0-SNAPSHOT.jar
#WORKDIR /opt/flink
#COPY --from=maven --chown=flink:flink /usr/app/${JAR_FILE} /opt/flink/pi3flinkpipeline-1.0d-SNAPSHOT.jar
