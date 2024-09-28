## API Gateways - KrakenD

An **API Gateway** is a critical component in modern microservices architecture, acting as a reverse proxy that sits between clients (web/mobile applications) and backend services. It provides a unified entry point for managing and routing requests to multiple microservices. The key functionalities of an API Gateway include:

- **Routing:** Directs client requests to the appropriate backend service based on the request path or other criteria.
- **Load Balancing:** Distributes incoming traffic evenly across multiple instances of backend services to improve performance and availability.
- **Authentication and Authorization:** Secures APIs by validating client credentials and ensuring authorized access.
- **Rate Limiting and Throttling:** Prevents abuse by limiting the number of requests from clients within a certain period.
- **Request Transformation:** Modifies incoming requests and outgoing responses (e.g., changing formats or adding/removing headers).
- **Circuit Breaking and Failover:** Handles failures gracefully by redirecting requests to alternative services or providing fallback responses.
- **Logging and Monitoring:** Captures detailed information on each request and response for monitoring and debugging purposes.

API Gateways simplify the complexity of managing multiple microservices and provide a consistent interface to external clients.

**KrakenD** is an open-source, high-performance API Gateway built with Go (Golang) and designed to handle high loads with low latency. It provides a lightweight and stateless way to manage APIs with minimal resource consumption.

### Key Features of KrakenD:

1. **Declarative Configuration:** KrakenD uses a configuration file (`config.json` or `config.yml`) to define services, endpoints, and middleware, eliminating the need to write custom code.
2. **Backend Aggregation:** Combines responses from multiple backend services into a single API response, reducing the number of network calls.
3. **Performance and Scalability:** Built with Go, KrakenD is highly performant and can handle high throughput with low latency.
4. **Middleware and Plugins:** Supports custom middleware and plugins for various functionalities, such as authentication, logging, rate limiting, and more.
5. **Stateless and Lightweight:** Each request is processed independently, making it easy to scale KrakenD horizontally.
6. **Security:** Provides authentication mechanisms like OAuth2, API keys, and JWT (JSON Web Token) validation.

---------

### API Gateway Questions

1. **What is an API Gateway, and why is it used?**

   **Answer:**  
   An API Gateway is a server that sits between the client and backend services. It acts as a reverse proxy to route client requests to the appropriate service and handle tasks such as request/response transformation, authentication, rate limiting, logging, and monitoring.

   - **Use Cases**:
     - Request Routing: Direct client requests to the appropriate microservices.
     - Security: Implement security mechanisms like OAuth2 and API keys.
     - Load Balancing: Distribute requests across multiple service instances.
     - Rate Limiting: Limit the number of requests a client can make within a specified time window.
     - Analytics and Monitoring: Collect and analyze request metrics and logs.

2. **How does an API Gateway differ from a Load Balancer?**

   **Answer:**  
   - **API Gateway**:
     - Handles more than just routing; it manages cross-cutting concerns such as authentication, rate limiting, and response transformation.
     - Routes requests to microservices based on paths and headers.
     - Suitable for managing microservices architectures.

   - **Load Balancer**:
     - Distributes network traffic across multiple servers or instances.
     - Operates at the network level (layer 4) or application level (layer 7).
     - Primarily focuses on balancing load and ensuring availability.

   - **Comparison**:

     - API Gateway:
       - Manages requests based on APIs, paths, and headers.
       - Provides security, monitoring, and logging.
       - Suited for microservices.

     - Load Balancer:
       - Balances load based on server health and availability.
       - Focuses on distributing traffic.
       - Suited for general traffic load balancing.

3. **What are some common features of API Gateways?**

   **Answer:**
   - Request Routing: Direct incoming API requests to appropriate backend services based on routes.
   - Authentication and Authorization: Implement security policies, validate tokens, and enforce access control.
   - Rate Limiting and Throttling: Limit the number of requests a client can make.
   - Caching: Cache responses to reduce backend load and improve performance.
   - Load Balancing: Distribute requests across multiple service instances.
   - Request/Response Transformation: Modify headers, query parameters, or request/response body.
   - Monitoring and Analytics: Collect logs, metrics, and traces for analysis.
   - Circuit Breaker: Protect services from cascading failures by managing fallback mechanisms.

4. **What is the difference between a Reverse Proxy and an API Gateway?**

   **Answer:**  
   - A Reverse Proxy directs client requests to a set of backend servers based on load balancing or other policies, without modifying or managing API-specific logic.
   - An API Gateway provides more extensive features like routing based on API paths, request/response transformation, security, and monitoring.

   - **Comparison**:

     - Reverse Proxy:
       - Focuses on routing and load balancing.
       - Does not provide API-specific features like rate limiting or authentication.
       - Example: Nginx, HAProxy.

     - API Gateway:
       - Handles complex routing, security, and service orchestration.
       - Manages cross-cutting concerns for APIs.
       - Example: Kong, KrakenD, AWS API Gateway.

5. **What are some popular API Gateway tools, and how do they compare?**

   **Answer:**  
   - **Kong**:
     - Open-source, extensible API Gateway built on NGINX.
     - Supports plugins for authentication, logging, rate limiting, and monitoring.
     - Highly customizable with Lua scripts.

   - **KrakenD**:
     - High-performance, stateless API Gateway designed to aggregate and transform API responses.
     - Focuses on low latency and provides a declarative configuration model.
     - Suitable for microservices and service mesh architectures.

   - **AWS API Gateway**:
     - Fully managed service that allows you to create and publish APIs at any scale.
     - Integrates seamlessly with other AWS services (Lambda, DynamoDB).
     - Supports RESTful APIs and WebSocket APIs.

   - **Azure API Management**:
     - Offers a complete API management platform with features like caching, rate limiting, and API versioning.
     - Integrates with Azure services for monitoring and analytics.

   - **Apigee**:
     - Enterprise-grade API management platform with advanced security, analytics, and monetization features.
     - Suitable for large-scale enterprises needing API governance.

6. **What is a circuit breaker pattern, and how does it apply to an API Gateway?**

   **Answer:**  
   The circuit breaker pattern is a design pattern used to detect and handle service failures gracefully. It prevents an API Gateway from making repeated requests to an unresponsive service by "tripping" the circuit when failures exceed a threshold.

   - **How it works**:
     - Closed State: All requests are allowed to pass through.
     - Open State: Requests are blocked, and an error is returned immediately without contacting the backend service.
     - Half-Open State: A limited number of requests are allowed through to check if the backend service has recovered.

   - **Application in API Gateways**:
     - API Gateways use this pattern to manage service failures and provide fallback mechanisms, such as returning cached responses or directing traffic to a different service instance.

   - **Benefits**:
     - Protects services from cascading failures.
     - Improves the overall reliability and availability of the system.

7. **What is API Gateway rate limiting, and how is it implemented?**

   **Answer:**  
   Rate Limiting is a technique used to control the number of requests a client can make to an API within a specific timeframe. It helps prevent abuse, protects backend services from overload, and ensures fair usage of resources.

   - **Implementation**:
     - Based on client identity (API key, IP address).
     - Configurable policies like X requests per second/minute/hour.
     - Implemented using built-in plugins or third-party libraries.

   - **Types of Rate Limiting**:
     - Fixed Window: Limits requests in a fixed time window (e.g., 1000 requests per hour).
     - Sliding Window: Dynamically adjusts the rate limit based on a rolling window of time.
     - Token Bucket: Uses a token bucket algorithm to allow bursts of traffic while maintaining overall rate limits.

   - **Implementation Example**:
     - In Kong, use the `rate-limiting` plugin:
       ```yaml
       plugins:
         - name: rate-limiting
           config:
             second: 5 # 5 requests per second
             minute: 100 # 100 requests per minute
             policy: local
       ```

8. **How do you secure APIs using an API Gateway?**

   **Answer:**  
   API Gateways provide several mechanisms to secure APIs, including:

   - Authentication:
     - Validate client identity using OAuth2, JWT, API keys, or custom authentication mechanisms.

   - Authorization:
     - Enforce permissions and access control based on roles or scopes.

   - Rate Limiting:
     - Limit the number of requests a client can make within a time window to prevent abuse.

   - TLS/SSL Encryption:
     - Encrypt data in transit using HTTPS and manage certificates.

   - IP Whitelisting/Blacklisting:
     - Restrict access to specific IP addresses or ranges.

   - Request Validation:
     - Validate request headers, query parameters, and payloads to ensure they conform to the expected schema.

   - Content Security Policies:
     - Implement security headers and policies to protect against common attacks like XSS and CSRF.

9. **What are some common challenges in implementing an API Gateway?**

   **Answer:**  
   - Performance Overhead:
     - API Gateways add an additional network hop, introducing latency and performance overhead.

   - Single Point of Failure:
     - A poorly configured API Gateway can become a bottleneck or a single point of failure for the entire system.

   - Complex Configuration and Management:
     - Managing routes, security policies, rate limiting, and monitoring for large-scale applications can become complex.

   - Scalability:
     - Scaling an API Gateway to handle high volumes of traffic requires careful planning, including distributed deployments and load balancing.

   - Debugging and Troubleshooting:
     - Troubleshooting issues through an API Gateway can be challenging due to the additional layer of abstraction and the need to correlate logs and metrics across services.

---------

Others:

- Setup working condition: Works.
- Note that I tried integrating Kong API Gateway in the beginning, but was running into issues in cross service communication. Hence, had to switch to KrakenD. Issue raised: https://github.com/Kong/kong/issues/13512
- Also, tried using config.json instead of yml format, but was running into issues, hence fall back to yml way of defining. Similar changes made in service defined in docker compose file as well. 

---------
