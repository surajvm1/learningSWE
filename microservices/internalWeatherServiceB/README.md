## Microservice - internalWeatherService

- The microservice does 2 things:
  - When the frontend GET requests temperature for a specific location: The service returns data points for a location by sequentially checking in our internal db's, i.e read through Redis cache, Postgres, Mongo. If it doesn't find the relevant data, then it calls an externalService to get the data.
    - Sends response to frontend via API gateway/ LB, and also wraps the data in an event and publishes to Kafka.
  - Similarly, executes POST/PUT/DELETE API calls. 

---------

Others:

- Setup working condition: Working. 
- Note there were problems setting up connecting to Mongodb container: So had to add `authSource=admin` in the mongodb uri. [Ref link](https://stackoverflow.com/questions/72048051/pymongo-auth-failure-ok-0-0-errmsg-authentication-failed-code-18).

---------
