package pi3flinkpipeline;

import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class DataStreamJob {
	public static void main(String[] args) throws Exception {
		// Set up the execution environment
		final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
		// Define the Kafka source
		KafkaSource<String> kafkaSource = KafkaSource.<String>builder()
				.setBootstrapServers("localhost:29092")
				.setTopics("topic_splitpay") // Replace with your Kafka topic name
				.setGroupId("flink-group")
				.setStartingOffsets(OffsetsInitializer.earliest())
				.setValueOnlyDeserializer(new SimpleStringSchema())
				.build();
		// Create a DataStream from the Kafka source
		DataStream<String> stream = env.fromSource(
				kafkaSource,
				WatermarkStrategy.noWatermarks(),
				"Kafka Source"
		);
		// Process the stream
		stream.map(DataStreamJob::parseEventAndInsertToPostgres);
		// Execute the Flink job
		env.execute("Kafka to PostgreSQL Job");
	}
	// Method to parse JSON and insert into PostgreSQL
	private static String parseEventAndInsertToPostgres(String event) {
		try {
			// Jackson ObjectMapper instance
			ObjectMapper objectMapper = new ObjectMapper();
			// Parse the JSON event
			JsonNode jsonEvent = objectMapper.readTree(event);
			String eventId = jsonEvent.get("event_id").asText();
			String userName = jsonEvent.get("data").get("user").asText();
			String location = jsonEvent.get("data").get("location").asText();
			// JDBC connection details as defined in docker compose file
			String jdbcUrl = "jdbc:postgresql://localhost:5432/pi3db";
			String jdbcUser = "admin_suraj";
			String jdbcPassword = "pws_suraj";
			// Insert parsed data into PostgreSQL
			try (Connection connection = DriverManager.getConnection(jdbcUrl, jdbcUser, jdbcPassword)) {
				String sql = "INSERT INTO events (event_id, user_name, location) VALUES (?, ?, ?)";
				try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
					preparedStatement.setString(1, eventId);
					preparedStatement.setString(2, userName);
					preparedStatement.setString(3, location);
					preparedStatement.executeUpdate();
				}
			}
			// Return the event as is for potential further processing
			return event;
		} catch (Exception e) {
			e.printStackTrace();
			return null;
		}
	}
}
