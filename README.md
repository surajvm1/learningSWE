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

krakend context deadline exceeded error - increase timeout


https://stackoverflow.com/questions/62198606/kafkatimeouterror-failed-to-update-metadata-after-60-0-secs

urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='external_service_a', port=9900): Max retries exceeded with url: /externalApi/getWeather/delhi (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0xffff94ecda30>: Failed to establish a new connection: [Errno 111] Connection refused'))

https://serverfault.com/questions/967580/chmod-changing-permissions-of-myscript-sh-operation-not-permitted

https://stackoverflow.com/questions/68126583/kafka-connect-failed-to-connect-to-localhost-port-8083-connection-refused

kafka-topics --bootstrap-server localhost:29092 --list
kafka-topics --bootstrap-server kafka:9092 --list

-> running this to create topic in kafka terminal: kafka-topics --create --topic topic_a --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
and then running producer consumer code

https://github.com/confluentinc/cp-docker-images/issues/272
inside debezium container: curl -X POST -H "Content-Type: application/json" --data @/kafka/config/debezium_connector_config.json http://debezium:8083/connectors

run kafka consumer as fastapi application on 2 ports

have project in java, go, backend also for learnign

debezium akfka connect script execution timing delayed as it was hanging to continuing to cehck akfak connect long long, when i logged into container and executed script it worked, so better have to wait for sometime and then only execute script

curl -s -o /dev/null -w ''%{http_code}'' http://localhost:8083/connectors
curl -s -o /dev/null -w ''%{http_code}'' http://debezium:8083/connectors

https://www.reddit.com/r/docker/comments/1f1wqnb/how_i_reduced_docker_image_size_from_588_mb_to/

when i add cmd step to trigger an sh script running a curl command in compose file, i am not getting any status of container, but when i run container normally and logging to it and then run curl commadn manually i get the container with proper status code, why?

 podman-compose -f temp-compose.yml up --build --no-cache 

podman logs debezium | less
podman history quay.io/debezium/connect:latest
podman inspect debezium
podman-compose -f temp-compose.yml up -d --build --force-recreate
podman image inspect quay.io/debezium/connect:latest

podman ps -aq -> show containers which are in exit state
podman rm -f $(podman ps -aq)
podman compose down
sudo lsof -i -P | grep LISTEN | grep :8003

podman-compose -f temp-compose.yml up --build --no-cache        

https://www.docker.com/blog/docker-best-practices-choosing-between-run-cmd-and-entrypoint/
https://ollama.com/library/llama3.1
https://hub.docker.com/r/debezium/postgres
https://docs.docker.com/reference/dockerfile/#entrypoint
https://github.com/debezium/debezium-examples/blob/main/tutorial/docker-compose-postgres.yaml
https://stackoverflow.com/questions/30063907/docker-compose-how-to-execute-multiple-commands
https://quay.io/repository/debezium/connect?tab=info
https://hub.docker.com/r/debezium/connect
https://github.com/debezium/container-images/blob/main/connect-base/3.0/Dockerfile
https://hub.docker.com/r/debezium/connect/tags?page=&page_size=&ordering=&name=sha256%3A4f5ff656580bbf4228bbadf94f0fd36311db5877586532347c9ef1e1daa66c28
https://stackoverflow.com/questions/41694329/docker-run-override-entrypoint-with-shell-script-which-accepts-arguments
https://stackoverflow.com/questions/4421633/who-is-listening-on-a-given-tcp-port-on-mac-os-x
https://dev.to/kittipat1413/docker-run-vs-cmd-vs-entrypoint-demystifying-the-differences-2a4p

https://www.dbi-services.com/blog/postgresql-when-wal_level-to-logical/
https://github.com/bitnami/charts/issues/6830


psql -U postgres_user_suraj -d weatherdb
SHOW wal_level; (definitely put semi colon)

root@1d86a12c71f9:/# psql -U postgres_user_suraj -d weatherdb
psql (13.16 (Debian 13.16-1.pgdg120+1))
Type "help" for help.

weatherdb=# SHOW wal_level;
 wal_level 
-----------
 logical
(1 row)

weatherdb=# ALTER SYSTEM SET wal_level = logical;
ALTER SYSTEM
weatherdb=# 
weatherdb=# select * from weather limit 10;

https://sqlalche.me/e/14/e3q8

https://stackoverflow.com/questions/30848670/how-to-customize-the-configuration-file-of-the-official-postgresql-docker-image?rq=3




weatherdb=# SELECT * FROM pg_stat_replication;
 pid | usesysid |       usename       |  application_name  | client_addr | client_hostname | client_port |         backend_start         | backend_xmin |   state   | sent_lsn  | write_lsn | flush_lsn | replay_lsn | write_lag | flush_lag | replay_lag | sync_priority | sync_state |          reply_time           
-----+----------+---------------------+--------------------+-------------+-----------------+-------------+-------------------------------+--------------+-----------+-----------+-----------+-----------+------------+-----------+-----------+------------+---------------+------------+-------------------------------
  38 |       10 | postgres_user_suraj | Debezium Streaming | 10.89.0.218 |                 |       55018 | 2024-08-31 18:16:15.936886+00 |              | streaming | 0/15F77C0 | 0/15F77C0 |           |            |           |           |            |             0 | async      | 1999-12-21 01:02:35.607882+00


https://severalnines.com/blog/using-postgresql-replication-slots/

[appuser@c8150e92e7d3 ~]$ kafka-topics --list --bootstrap-server localhost:9092
__consumer_offsets
dbserver1.public.weather
debezium_config
debezium_offset
debezium_status
topic_a

https://medium.com/@oredata-engineering/setting-up-prometheus-grafana-for-kafka-on-docker-8a692a45966c

https://www.tutorialsteacher.com/python/classmethod-decorator

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 sparkStream.py
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 sparkStream.py

do load balancing and see APIs

chmod +x register_schema.sh: chmod +x on a file (your script) only means, that you'll make it executable.

https://stackoverflow.com/questions/40714583/how-to-specify-a-port-to-run-a-create-react-app-based-project

grafana password username: admin, admin

https://stackoverflow.com/questions/74029504/spring-prometheus-grafana-err-reading-prometheus-post-http-localhost90
hence in grafana, i had to use this url: http://prometheus:9090/

google cadvisor on another website


https://github.com/google/cadvisor/issues/1843
https://stackoverflow.com/questions/71977532/podman-mount-host-volume-return-error-statfs-no-such-file-or-directory-in-ma

kafka-topics --bootstrap-server kafka:9092 --list
topic_splitpay

kafka-consumer-groups --bootstrap-server kafka:9092 --version

kafka-console-consumer --bootstrap-server localhost:9092 --topic topic_splitpay --from-beginning
-- to view all messages inside kafka

What's the difference between ARM and x86? ARM architecture uses a RISC approach for efficiency and lower power, ideal for mobile devices. x86 employs a CISC approach for high performance, suited for desktops and servers. What is register-based processing?

add monitoring to the system,

add flink also in the system integrate it... 

add 



#deebzium push???event
#kafka schema registry also implement???
#docker image version be specific
#UI on nginx, kafka krakend???

alerting promethusm to addd. 

load balancing to do of the APIs 




podman-compose up --build

podman build --no-cache -t img .


To start project: 
Login to weather app website and replce env service key: 

starting react web app

starting microservices
 










