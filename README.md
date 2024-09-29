## Project Overview

- End goal (rough):
![project architecture overview](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/e2eDevProj.drawio.png)

- Note(s): 
  - Project done in past to understand docker services: https://github.com/surajvm1/LearningMicroservices
  - Repo, where I save my learnings from internet: https://github.com/surajvm1/mDumpSWE

- Things to do in project in the future: 
  - Integrate monitoring tools in services like Prometheus/Grafana/cAdvisor. 
  - Have an ML model integrated listening to events in real-time and sending back a response. 
  - Increase the complexity of project by adding more features eg: Authentication, etc. Can also write services in Go/Ruby, etc., languages based on learning. 
  - Check issues faced integrating Kong API gateway. Converge load balancer and API gateway to a single service, to avoid many hops. 
  - Load test the service using ab, k6, etc. 
  - Add more features to Debezium CDC to better capture tables states. 
  - Deploy service to AWS/GCP cloud for more learning. 
  - Fix/Integrate mobile app, flink. 
  - Implement Kafka schema registry. 
  - Use kubernetes. 
  - Go in depth to each of these services for more learning. 

----------------------------------------

### Project setup

- Ensure you have below technologies installed on your machine. Machine I am using: Mac. 
  - Python (v3.9.6); And Python virtualenv as well.  
  - Javascript
  - FastAPI
  - NodeJS (eg: `v20.15.1`)
  - ReactJS 
  - Docker/Podman desktop
  - Spark (v3.4.1)
  - Compose (Docker or Podman compose)
  - IDEs for development
  - Git 
  - Others:
    - Java (v11)

- To start running the project on your local; Follow: 

```
First:
Start with running the frontend web app service. 
  cd webFrontend/webapp
  npm install 
  npm start
This will start the frontend server at http://localhost:4200/

Second:
I am using podman locally to run microservices. Ensure you have done basic setup of podman, creating podman machine etc. Docker can also be used, and commands remain same, all one has to do is replace command having podman keyword to docker. 
Make the file executable in debezium folder: 
  cd microservices/debezium
  chmod +x setup.sh
Update the API key to yours in: 
  cd microservices/externalServiceA
  vi .env 
Add your API key rather than using mine. To add/create new API key go to and create account in: https://www.weatherapi.com/ and use the weather API key from there. 
Spin up the microservices from: 
  cd microservices
  podman-compose up --build --no-cache ## Note that if using docker, use docker-compose command. Arguments remain same. 
You may get an error like: debezium | Caused by: org.postgresql.util.PSQLException: ERROR: logical decoding requires wal_level >= logical
You have to change wal_level. For this what you must do is login to your postgres container and run below commands, in my case as per project it is: 
Note that you could rather than executing commands from terminal, also go into the container shell and do the processes from podman or docker desktop - you will save few steps. 
  podman ps
  podman exec -it postgres_service bash 
  psql -U postgres_user_suraj -d weatherdb
  SHOW wal_level;
  ALTER SYSTEM SET wal_level=logical;
  exit
  exit
  podman restart postgres_service
  podman exec -it postgres_service bash 
  psql -U postgres_user_suraj -d weatherdb
  SHOW wal_level;
  ## Ensure your wal_level is changed to logical - else debezium won't be able to listen and capture table changes.

Third: 
At this point most of your services would start, some may have started and stopped probably due to some cyclic dependency, you can view them using ps command or the docker/podman desktop and restart them again. 

Fourth: 
All the data/events that are emitted in the services, would be saved in Desktop. To ensure it saves in your local machine desktop; 
Navigate to the folder: 
  cd microservices
There, notice I have used this volume: /Users/suraj/Desktop in the consumers I have written. Change them to your local machine Desktop path. 

Fifth: 
Start spark streaming by (ensure you have setup pyspark locally to submit to spark); 
But ensure you have first run the web app, so that kafka topics are created on the fly and atleast 1 event is emitted. As, in code, we setup the kafka topic on the fly once atleast 1 event is sent. We could also manually create topics going inside container as well, and then start spark streaming, but to make life easier, lets, emit atleast 1 event and then start spark.
Else spark would give an error like this: pyspark.errors.exceptions.captured.StreamingQueryException: [STREAM_FAILED] Query [id = 29ce6efd-a5e7-4ecd-85a0-846203c5ed89, runId = a34864b7-eb33-44a8-8016-1eb3f37a9183] terminated with exception: org.apache.kafka.common.errors.UnknownTopicOrPartitionException: This server does not host this topic-partition.
Emitting an event, means, simply go to the web app and try GET'ing the weather of a city, as it fetches the weather, it will listen to this action and publish the event in Kafka. Do it once, and then start spark streaming, so that then subsequent actions are anyways recorded.
Navigate to: 
  cd dataStreaming/pyspark
  spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 sparkStream.py
  
Note: 
  Debezium will capture changes in postgres table only during POST calls, when you insert any data in db, during other calls, it may not capture the state of the db.
  
```

----------------------------------------

### Project Images for reference

![all-containers.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/all-containers.png)

![get-api-call.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/get-api-call.png)
![post-api-call.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/post-api-call.png)
![update-api-call.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/update-api-call.png)
![delete-api-call.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/delete-api-call.png)

![nginx-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/nginx-logs.png)
![krakend-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/krakend-logs.png)

![kafka-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/kafka-logs.png)
![zookeeper-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/zookeeper-logs.png)
![kafka-topics.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/kafka-topics.png)

![redis-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/redis-logs.png)
![postgres-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/postgres-logs.png)
![postgres-table-data.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/postgres-table-data.png)
![mongodb-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/mongodb-logs.png)

![debezium-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/debezium-logs.png)

![internal-service-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/internal-service-logs.png)
![external-service-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/external-service-logs.png)
![kafka-producer-logs.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/kafka-producer-logs.png)

![spark-stream-logs1.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/spark-stream-logs1.png)
![spark-stream-logs2.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/spark-stream-logs2.png)

![backend-service-data.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/backend-service-data.png)
![debezium-data.png](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/debezium-data.png)

----------------------------------------
