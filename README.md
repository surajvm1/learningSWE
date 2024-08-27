## Project Overview

- End goal (rough):
![project architecture overview](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/e2eDevProj.drawio.png)

- Note: Project done in past to understand docker services: https://github.com/surajvm1/LearningMicroservices
To increase complexity of project may add: integrate with ML model, write services in java/go and not just python, add more features to app and make some better usecase

----------------------------------------

(Rough set up updates in project - will clean up readme later)

Download nodejs
 2426  cd webFrontend
 2429  npx create-react-app webapp (all small case)
 2430  cd webapp
 2437  node -v
 2431  npm start

cleanup unnecessary files

 npm install axios

npm install react-router-dom

coding routes and basic code

python service
 2482  cd microservices
 2483  ls
 2484  python3 -m venv microServiceB
 2485  cd microServiceB
 2486  source bin/activate
 2487  pip freeze

pip install fastapi requests "uvicorn[standard]" SQLAlchemy==1.4.46 psycopg2-binary pydantic pandas redis

# to run fastapi service: podman build --no-cache -t internal_weather_service_b_image . 
# podman run -p 8900:8900 --name internalWeatherServiceBCon internal_weather_service_b_image

# to run the compose file: podman-compose up --build

nodemon install: sudo npm install -g --force nodemon
but note its for nodejs proejcts not react projects... 



brew install nginx       
brew services start nginx
it runs in 8080 port
cd /opt/homebrew/etc/nginx

making changes in the config file
here in project added config file just for reference how it looks like
paralelly setup kong gatewaymicroservice

307 is a type of temporary redirect. This HTTP response status code means that the URL someone is requesting has temporarily moved to a different URI (User Resource Identifier), but will eventually be back in its original location.

A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it.

https://semaphoreci.com/blog/custom-middleware-fastapi

debug using middleware kong issue??
https://stackshare.io/stackups/pypi-confluent-kafka-vs-pypi-kafka-python

https://github.com/Kong/kong/issues/13512

docker vs virtual machine - understand more in detail, somethings seem a little vague for my understanding. 



https://www.reddit.com/r/macgaming/comments/10wb6k5/what_exactly_is_rosetta/

https://stackoverflow.com/questions/47710767/what-is-the-alternative-to-condition-form-of-depends-on-in-docker-compose-versio

i get Error: unable to start container 7d894592e938ccf2c05115ff41e325cc1970fcce198b6fa04479bf99e1db8f36: preparing container 7d894592e938ccf2c05115ff41e325cc1970fcce198b6fa04479bf99e1db8f36 for attach: generating dependency graph for container 7d894592e938ccf2c05115ff41e325cc1970fcce198b6fa04479bf99e1db8f36: container 8bcd4866f6d4899e50f445ed111d9df1dce063ece75c13c2c523587e423921e5 depends on container b369eb05745b14a5e57f107f55789905b78788f2ec60cda8dd6dc2564fb4caee not found in input list: no such container
when i run in docker/podman compose,  is there a way to increase timeout of interdependent containers?
tried adding health check, increasing timeout
podman-compose up --timeout 300
or
  kafka:
    image: confluentinc/cp-kafka:latest
    container_name: kafka
    depends_on:
      - zookeeper
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    ports:
      - "9092:9092"
    healthcheck:
      test: ["CMD", "kafka-broker-api-versions", "--bootstrap-server", "localhost:9092"]
      interval: 10s
      timeout: 5s
      retries: 5
but it did not work, hence for now removed depends_on for kafka in debezium in compose... and  letting debezium up regardless kafka or zookeeper goes up or not
the bug needs to be debugged, apart from different bugs observed in project

