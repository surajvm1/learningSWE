## Streaming Systems - Spark & Flink

Apache Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams. 

- **Key Features**:
  - Supports both batch and streaming workloads.
  - Processes data from various sources such as Kafka, Kinesis, and TCP sockets.
  - Utilizes Discretized Streams (DStreams) to represent streaming data divided into small batches.
  - Integrates seamlessly with other Spark components like MLlib and Spark SQL.

- **Processing Model**:
  - Receives live input data streams and divides them into batches.
  - Processes these batches using the Spark engine to generate results.
  - Allows for complex algorithms expressed through high-level functions like map, reduce, join, and window.

- **Recovery and Fault Tolerance**:
  - Automatically recovers lost work and operator state without additional code.
  - Provides fast recovery from failures and better load balancing.

- **Programming Languages Supported**:
  - Java, Scala, and Python.

Apache Flink is an open-source, distributed engine designed for stateful processing over unbounded (streams) and bounded (batches) datasets.

- **Key Features**:
  - Supports low-latency processing with in-memory computations.
  - Guarantees exactly-once state consistency even in case of failures.
  - Provides advanced state management and event-time processing semantics.
  - Offers a unified programming model for both stream and batch processing.

- **Processing Model**:
  - Ingests data streams continuously and performs computations or transformations.
  - Stores results as states within Flink, allowing for output as data streams to other systems.

- **Use Cases**:
  - Event-driven applications (e.g., fraud detection, real-time analytics).
  - Data pipelines for real-time ETL processes.
  - Streaming analytics for monitoring live data.

- **Programming Languages Supported**:
  - Java, Scala, Python, and SQL.

Comparison of Spark Streaming and Flink

| Feature                     | Apache Spark Streaming                         | Apache Flink                              |
|-----------------------------|-----------------------------------------------|------------------------------------------|
| Processing Model             | Micro-batch processing                        | Continuous stream processing              |
| Latency                      | Higher latency due to micro-batching         | Low latency with in-memory processing     |
| State Management             | Supports stateful processing                  | Advanced state management with exactly-once guarantees |
| Fault Tolerance              | Automatic recovery of lost work               | Built-in fault tolerance with state consistency |
| API Complexity               | Higher complexity due to micro-batching      | Unified API for both batch and stream    |
| Use Cases                   | Batch jobs with streaming capabilities        | Real-time event-driven applications       |

Conclusion

Both Apache Spark Streaming and Apache Flink serve the purpose of stream processing but differ significantly in their architecture, processing models, and use cases. Spark Streaming is suitable for scenarios where batch processing is also required, while Flink excels in low-latency applications that demand continuous data processing. Choosing between them depends on specific project requirements such as latency needs, complexity, and integration capabilities.

---------

Others:

- Setup working condition: Works for pyspark. Flink setup - Developed it separately as a project since it requires Java to work on. And have just added those files in the current Python-JS ecosystem weather app project, will have to check what tweaking to be done to integrate in current project. But standalone if I have to run just the flink setup with Java 11, it will work. 
- Some more details on spark & flink: https://github.com/surajvm1/mDumpSWE

---------