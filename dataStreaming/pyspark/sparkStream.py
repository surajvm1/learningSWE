from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, IntegerType

# Create a Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

# Define the schema for the JSON data
json_schema = StructType() \
    .add("location", StringType()) \
    .add("temperature", IntegerType()) \
    .add("timestamp", StringType()) \
    .add("service", StringType())

# Read data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:29092") \
    .option("subscribe", "topic_a") \
    .load()

# Parse the JSON data
parsed_df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), json_schema).alias("data")) \
    .select("data.*")

# Count the number of records
count_query = parsed_df.writeStream \
    .outputMode("update") \
    .format("console") \
    .start()

# Keep the application running
count_query.awaitTermination()