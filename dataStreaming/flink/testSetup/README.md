
### Notes: 

**Important: This is a standalone flink setup for learning. I have not yet integrated it in the current weatherApp project. Its WIP.**

Intention of the is to help setup and understand end-to-end flink pipeline on local system in Mac. 
- The flow looks like this: Kafka producer -> Kafka -> Flink streaming consumer -> Postgres table
- We produce sample events to Kafka which is later consumed by Flink, some parsing of data happens in realtime and we publish this in Postgres table.

Before we start we must install few things on Mac and some info around basic setup, you can google it or use the commands if given: 
- Podman/Docker Desktop - At Simpl, we have recently switched from Docker to Podman, so use Podman related utilities (It's very similar to Docker in commands, and architecture) 
- Docker/Podman compose 
- IntelliJ IDE for Java Community Edition - Setup the IDE to support Flink. View below image for reference on what options to choose when creating a new Project. 
  - ![utilites/flinksetup image](https://github.com/GetSimpl/pi3-flink-pipeline/blob/main/readme_file_utilities/flinksetup.png)
  - Post that your project would be auto-created by IDE with a folder structure. There are 2 main files to focus. 
    - `pipeline/pom.xml` - This file is similar to what we have in Python ecosystem as requirements.txt. In the xml file, we define the Maven dependencies or packages we want to use in our project. For our learning, we can use the dependencies defined in the current commit. Also, if we read the pom xml file. I have added a basic info on how the different components of the xml file, same can be googled and read about. [Maven: Command to update repository after adding dependency to POM](https://stackoverflow.com/questions/8563960/maven-command-to-update-repository-after-adding-dependency-to-pom). You can search for maven packages [from here](https://mvnrepository.com/search?q=flink). Just like we have Maven as a build system in Java, we also have Gradle, depending on a comfort one may choose any. 
    - `pipeline/src/main/java/pi3flinkpipeline/DataStreamJob.java` - This is the main file which runs my Flink code. So in short, when I locally run a kafka producer and publish data to kafka container, the code inside DataStreamJob.java keeps listening to the Kafka messages from topic, does some processing and loads data in a postgres table which is again running via docker container. 
    - Note that I have also created a `Dockerfile - which is empty`, `pipeline/src/main/resources/configs/<properties> files` - You can ignore that for now. 
    - Also, there can be cases where the IDE is making your files as non project files; Mostly it's due to corrupt `.idea` file, but you can also [refer this link to debug](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360010640479-all-files-in-my-project-became-non-project). 
- Install Java 11 via brew for Flink ecosystem (prefer) or google it. 
- Install Python 3.9+ locally to run basic Kafka producer code.
- Install git for version control. And can see I have added a sample `.gitignore` file. 
- Install maven using: `brew install maven`. In your pom.xml directory install the packages/dependencies in your project using: `mvn clean install`. You can install new packages using: `mvn install <package name>`. 
- Now understand this; When you build and run your java project having Flink, it generates a jar file. [What is jar file?](https://stackoverflow.com/questions/12079230/what-exactly-does-a-jar-file-contain). This jar file is what we submit to a Flink job manager which later interprets the content inside the jar file and runs the parallel computation tasks which we expect. 
  - We can have Flink installed locally via: `brew install apache-flink` and start flink server on local, so when we run our java-flink code in IDE and it generates a jar file, we have to upload it to Flink job manager running on the server and submit it, later it interprets it and allocates resources to task managers and runs code. In our case, the jar file would be produced in this directory: `pipeline/target/pi3flinkpipeline-1.0-SNAPSHOT.jar`
    - If we go via this route, you have to locate a `start-cluster.sh` file in Flink package, you can refer [this link](https://superuser.com/questions/1376075/how-to-run-apache-flink-1-6-2-in-localhost) for context or in short understand that you have to cd to this path from terminal: `cd /opt/homebrew/Cellar/apache-flink/1.20.0/libexec` and then run: `./bin/start-cluster.sh`. Then you access Flink UI and do the above process as discussed. In case of failures, in UI you can navigate to job manager logs from: `Job Manager button on left -> Logs sub tab -> View the logs`.
  - (OR) You can make your IDE setup like flink which we have already done, if followed earlier tasks, and simply, click on the IDE's run button to run Flink code normally, just like we run a C/C++ program - this is easier. 
- I have defined Kafka producer code in: `localDevTesting/kafkaProducer/producer.py` where it simply, publishes a sample data to Kafka to a certain topic. The topic is created on the fly as we are using confluent_kafka library and it offers us this. Else we would have to run commands inside Kafka container to create topic and connect, etc. The code runs as a docker container, Dockerfile can be seen in same directory. 
- Now we take a step back, and I am running my Kafka, Zookeeper, Postgres via docker images defined in docker-compose file. 
- To start the project in testing/dev mode; Follow below steps: 
```
Step1: 
Be in the directory where docker-compose.yml file is present and: podman-compose up --build --no-cache or docker-compose up --build --no-cache 
This will start the services and start automatically publishing data in Kafka. 

You can verify this by going inside Kafka container and running few of below commands: 
To view kafka topics: kafka-topics --bootstrap-server kafka:9092 --list
To view kafka messages being published by the python kafka consumer: kafka-console-consumer --bootstrap-server localhost:9092 --topic topic_splitpay --from-beginning
To view consumer groups: kafka-consumer-groups --bootstrap-server localhost:29092 --list

Step2: 
Go to your pipeline/src/main/java/pi3flinkpipeline/DataStreamJob.java file and deep down you will find a flink sample code to run the whole setup, you can overwrite contents in file with commented code. 

Step3: 
Go to your postgres container via: podman exec -it postgres_service psql -U admin_suraj -d pi3db
Note that, admin_suraj and password, etc, I have defined in the docker-compose file in repo. 
Inside the postgres terminal, create a table via: 
CREATE TABLE events (
id SERIAL PRIMARY KEY,
event_id VARCHAR(50) NOT NULL,
user_name VARCHAR(50) NOT NULL,
location VARCHAR(100) NOT NULL
);
The table is named events with the fields. Understand that the event we are emitting in kafka has lots of details, but in flink consumer we clean up and parse the events and load only specific fields in postgres table, hence limited columns. 
Check if table created properly using: select * from events; (OR) \dt command. 

Step 4: 
Now data is being pushed to Kafka, we want flink to consume, parse and dump it postgres, so start the flink code, simply click on run button in the IDE, and your flink consumer will be running. We could also dockerfize and run it in a container, but that anyways in main project we will do, locally for understanding and testing, I have kept things simple.
```

Some snapshots of how the flow would look like:
![utilites/flinksetup image](https://github.com/GetSimpl/pi3-flink-pipeline/blob/main/readme_file_utilities/all_containers.png)
![utilites/flinksetup image](https://github.com/GetSimpl/pi3-flink-pipeline/blob/main/readme_file_utilities/kafka_producer_container_logs.png)
![utilites/flinksetup image](https://github.com/GetSimpl/pi3-flink-pipeline/blob/main/readme_file_utilities/flink_consuming_logs.png)
![utilites/flinksetup image](https://github.com/GetSimpl/pi3-flink-pipeline/blob/main/readme_file_utilities/postgres_table_count.png)

-----------------------

From flink docs, other good-resources: 
- https://nightlies.apache.org/flink/flink-docs-master/docs/concepts/flink-architecture/
- https://hackernoon.com/a-brief-history-of-flink-tracing-the-big-data-engines-open-source-development-87464fd19e0f
- https://blog.bytebytego.com/p/at-most-once-at-least-once-exactly
- https://medium.com/apache-kafka-from-zero-to-hero/apache-kafka-guide-3-producers-and-message-keys-a215e5fff75b

Good to start flink blogs/tutorials:
- https://m.mage.ai/getting-started-with-apache-flink-a-guide-to-stream-processing-70a785e4bcea
- https://nightlies.apache.org/flink/flink-docs-release-1.9/getting-started/tutorials/local_setup.html
- https://www.youtube.com/watch?v=deepQRXnniM&t=1500s
- https://www.youtube.com/watch?v=FoypLT2W91c&t=1850s

Flink is a distributed system and requires effective allocation and management of compute resources in order to execute streaming applications. It integrates with all common cluster resource managers such as Hadoop YARN and Kubernetes, but can also be set up to run as a standalone cluster or even as a library.
This section contains an overview of Flink’s architecture and describes how its main components interact to execute applications and recover from failures.
Anatomy of a Flink Cluster #
The Flink runtime consists of two types of processes: a JobManager and one or more TaskManagers.
The processes involved in executing a Flink dataflow
The Client is not part of the runtime and program execution, but is used to prepare and send a dataflow to the JobManager. After that, the client can disconnect (detached mode), or stay connected to receive progress reports (attached mode). The client runs either as part of the Java/Scala program that triggers the execution, or in the command line process ./bin/flink run ....
The JobManager and TaskManagers can be started in various ways: directly on the machines as a standalone cluster, in containers, or managed by resource frameworks like YARN. TaskManagers connect to JobManagers, announcing themselves as available, and are assigned work.
JobManager #
The JobManager has a number of responsibilities related to coordinating the distributed execution of Flink Applications: it decides when to schedule the next task (or set of tasks), reacts to finished tasks or execution failures, coordinates checkpoints, and coordinates recovery on failures, among others. This process consists of three different components:
ResourceManager
The ResourceManager is responsible for resource de-/allocation and provisioning in a Flink cluster — it manages task slots, which are the unit of resource scheduling in a Flink cluster (see TaskManagers). Flink implements multiple ResourceManagers for different environments and resource providers such as YARN, Kubernetes and standalone deployments. In a standalone setup, the ResourceManager can only distribute the slots of available TaskManagers and cannot start new TaskManagers on its own.
Dispatcher
The Dispatcher provides a REST interface to submit Flink applications for execution and starts a new JobMaster for each submitted job. It also runs the Flink WebUI to provide information about job executions.
JobMaster
A JobMaster is responsible for managing the execution of a single JobGraph. Multiple jobs can run simultaneously in a Flink cluster, each having its own JobMaster.
There is always at least one JobManager. A high-availability setup might have multiple JobManagers, one of which is always the leader, and the others are standby (see High Availability (HA)).
TaskManagers #
The TaskManagers (also called workers) execute the tasks of a dataflow, and buffer and exchange the data streams.
There must always be at least one TaskManager. The smallest unit of resource scheduling in a TaskManager is a task slot. The number of task slots in a TaskManager indicates the number of concurrent processing tasks. Note that multiple operators may execute in a task slot (see Tasks and Operator Chains).
Tasks and Operator Chains #
For distributed execution, Flink chains operator subtasks together into tasks. Each task is executed by one thread. Chaining operators together into tasks is a useful optimization: it reduces the overhead of thread-to-thread handover and buffering, and increases overall throughput while decreasing latency. The chaining behavior can be configured; see the chaining docs for details.
The sample dataflow in the figure below is executed with five subtasks, and hence with five parallel threads.
Operator chaining into Tasks
Task Slots and Resources #
Each worker (TaskManager) is a JVM process, and may execute one or more subtasks in separate threads. To control how many tasks a TaskManager accepts, it has so called task slots (at least one).
Each task slot represents a fixed subset of resources of the TaskManager. A TaskManager with three slots, for example, will dedicate 1/3 of its managed memory to each slot. Slotting the resources means that a subtask will not compete with subtasks from other jobs for managed memory, but instead has a certain amount of reserved managed memory. Note that no CPU isolation happens here; currently slots only separate the managed memory of tasks.
By adjusting the number of task slots, users can define how subtasks are isolated from each other. Having one slot per TaskManager means that each task group runs in a separate JVM (which can be started in a separate container, for example). Having multiple slots means more subtasks share the same JVM. Tasks in the same JVM share TCP connections (via multiplexing) and heartbeat messages. They may also share data sets and data structures, thus reducing the per-task overhead.
A TaskManager with Task Slots and Tasks
By default, Flink allows subtasks to share slots even if they are subtasks of different tasks, so long as they are from the same job. The result is that one slot may hold an entire pipeline of the job. Allowing this slot sharing has two main benefits:
A Flink cluster needs exactly as many task slots as the highest parallelism used in the job. No need to calculate how many tasks (with varying parallelism) a program contains in total.
It is easier to get better resource utilization. Without slot sharing, the non-intensive source/map() subtasks would block as many resources as the resource intensive window subtasks. With slot sharing, increasing the base parallelism in our example from two to six yields full utilization of the slotted resources, while making sure that the heavy subtasks are fairly distributed among the TaskManagers.
TaskManagers with shared Task Slots
Flink Application Execution #
A Flink Application is any user program that spawns one or multiple Flink jobs from its main() method. The execution of these jobs can happen in a local JVM (LocalEnvironment) or on a remote setup of clusters with multiple machines (RemoteEnvironment). For each program, the ExecutionEnvironment provides methods to control the job execution (e.g. setting the parallelism) and to interact with the outside world (see Anatomy of a Flink Program).
The jobs of a Flink Application can either be submitted to a long-running Flink Session Cluster, a dedicated Flink Job Cluster (deprecated), or a Flink Application Cluster. The difference between these options is mainly related to the cluster’s lifecycle and to resource isolation guarantees.
Flink Application Cluster #
Cluster Lifecycle: a Flink Application Cluster is a dedicated Flink cluster that only executes jobs from one Flink Application and where the main() method runs on the cluster rather than the client. The job submission is a one-step process: you don’t need to start a Flink cluster first and then submit a job to the existing cluster session; instead, you package your application logic and dependencies into a executable job JAR and the cluster entrypoint (ApplicationClusterEntryPoint) is responsible for calling the main() method to extract the JobGraph. This allows you to deploy a Flink Application like any other application on Kubernetes, for example. The lifetime of a Flink Application Cluster is therefore bound to the lifetime of the Flink Application.
Resource Isolation: in a Flink Application Cluster, the ResourceManager and Dispatcher are scoped to a single Flink Application, which provides a better separation of concerns than the Flink Session Cluster.
Flink Session Cluster #
Cluster Lifecycle: in a Flink Session Cluster, the client connects to a pre-existing, long-running cluster that can accept multiple job submissions. Even after all jobs are finished, the cluster (and the JobManager) will keep running until the session is manually stopped. The lifetime of a Flink Session Cluster is therefore not bound to the lifetime of any Flink Job.
Resource Isolation: TaskManager slots are allocated by the ResourceManager on job submission and released once the job is finished. Because all jobs are sharing the same cluster, there is some competition for cluster resources — like network bandwidth in the submit-job phase. One limitation of this shared setup is that if one TaskManager crashes, then all jobs that have tasks running on this TaskManager will fail; in a similar way, if some fatal error occurs on the JobManager, it will affect all jobs running in the cluster.
Other considerations: having a pre-existing cluster saves a considerable amount of time applying for resources and starting TaskManagers. This is important in scenarios where the execution time of jobs is very short and a high startup time would negatively impact the end-to-end user experience — as is the case with interactive analysis of short queries, where it is desirable that jobs can quickly perform computations using existing resources.

Streams are data’s natural habitat. Whether it is events from web servers, trades from a stock exchange, or sensor readings from a machine on a factory floor, data is created as part of a stream. But when you analyze data, you can either organize your processing around bounded or unbounded streams, and which of these paradigms you choose has profound consequences.
Bounded vs Unbounded
Batch processing is the paradigm at work when you process a bounded data stream. In this mode of operation you can choose to ingest the entire dataset before producing any results, which means that it is possible, for example, to sort the data, compute global statistics, or produce a final report that summarizes all of the input.
Stream processing, on the other hand, involves unbounded data streams. Conceptually, at least, the input may never end, and so you are forced to continuously process the data as it arrives.
In Flink, applications are composed of streaming dataflows that may be transformed by user-defined operators. These dataflows form directed graphs that start with one or more sources, and end in one or more sinks.
Programs in Flink are inherently parallel and distributed. During execution, a stream has one or more stream partitions, and each operator has one or more operator subtasks. The operator subtasks are independent of one another, and execute in different threads and possibly on different machines or containers.
The number of operator subtasks is the parallelism of that particular operator. Different operators of the same program may have different levels of parallelism.

Flink’s increasing popularity is founded largely on four building block components, namely its Checkpoint, State, Time, and Window mechanisms.
The Checkpoint mechanism is among Flink’s most important features. Flink implements distributed consistency snapshots based on the Chandy-Lamport algorithm, providing exactly-once semantics; by contrast, prior stream computing systems such as Strom and Samza did not effectively solve the exactly-once problem.
After providing consistent semantics, Flink introduces a managed state and provides API interfaces that users can manage states with while programming, making programming as easy as using Java sets.
Flink further implements the watermark mechanism that solves the data out-of-order and data late-arriving problems that occur in event-time based processing.
Finally, because stream computing is generally based on windows, Flink provides a set of out-of-box window operations including tumbling, sliding, and session windows, and supports flexible custom windows to meet special requirements.

----------------------

Other Infos:

Kafka commands:
```
Create a Topic : kafka-topics --bootstrap-server localhost:9092 --create --topic simpl-api-topic-local
Consumer offset: kafka-consumer-groups --bootstrap-server localhost:9092 --group Test --describe
Produce a message: kafka-console-producer --broker-list localhost:9092 --topic simpl-api-topic-local
Reset Offset: kafka-consumer-groups --bootstrap-server localhost:9092 --group Test --reset-offsets --to-latest --topic simpl-api-topic-local --execute
```

----------------------

