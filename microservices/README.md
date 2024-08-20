FastAPI Overview: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
ASGI Framework: FastAPI is built on ASGI (Asynchronous Server Gateway Interface), allowing for async and await capabilities for handling asynchronous tasks.

Dependencies: Define reusable logic and inject them into endpoints using Depends.
from fastapi import Depends

def get_query_param(q: str = None):
    return q

@app.get("/items/")
async def read_items(query_param: str = Depends(get_query_param)):
    return {"query_param": query_param}

Path and Query Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

Pydantic Models: Use Pydantic to define request and response models for data validation and serialization.
Data Validation: Automatically validates request payloads based on the Pydantic models.
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
@app.post("/items/")
async def create_item(item: Item):
    return item

Asynchronous Programming: FastAPI supports async functions, enabling handling of I/O-bound operations efficiently.
Database Operations: Use async database libraries (e.g., databases, SQLAlchemy with async support) to interact with databases asynchronously.

Authentication: Implement OAuth2, JWT tokens, or API key-based authentication.
Authorization: Protect routes with dependencies that check user permissions or roles.
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_jwt(token)  # Decode JWT token to get user info

Custom Middleware: Add middleware for tasks such as logging, CORS handling, or authentication.
from starlette.middleware.base import BaseHTTPMiddleware
class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['X-Custom-Header'] = 'Value'
        return response
app.add_middleware(CustomMiddleware)


ORM Integration: Use ORMs like SQLAlchemy, Tortoise ORM, or Pydantic’s BaseModel for database operations.

Use tools like pytest for unit and integration testing.

Background Tasks: Execute background tasks asynchronously using BackgroundTasks.
from fastapi import BackgroundTasks
@app.post("/send-notification/")
async def send_notification(background_tasks: BackgroundTasks, email: str):
    background_tasks.add_task(send_email, email)
    return {"message": "Notification sent"}



Docker:
# A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Here are the main components of a Dockerfile and explanations of when and how to use them:
# 1. FROM
# FROM <image>
# Description: Specifies the base image to use for the Docker image. This is the starting point for the build process.
# When to Use: Always, as it defines the base layer for your image.
# Example: FROM python:3.9-slim
# 2. LABEL
# LABEL key=value
# Description: Adds metadata to an image. Useful for providing information such as maintainer details or a version number.
# When to Use: When you want to include metadata in the image.
# Example: LABEL maintainer="you@example.com"
# 3. RUN
# RUN <command>
# Description: Executes a command in a new layer on top of the current image and commits the results. This is often used for installing packages.
# When to Use: When you need to install dependencies or run commands that are required to build your application.
# Example: RUN apt-get update && apt-get install -y gcc
# 4. COPY and ADD
# COPY <src> <dest>
# ADD <src> <dest>
# Description:
# COPY copies files and directories from the host file system to the image.
# ADD does the same as COPY but also supports extracting tar files and fetching files from URLs.
# When to Use: Use COPY for simple copying and ADD for additional functionalities.
# Example: COPY . /app
# 5. WORKDIR
# WORKDIR /path/to/workdir
# Description: Sets the working directory for any subsequent RUN, CMD, ENTRYPOINT, COPY, and ADD instructions.
# When to Use: When you want to set the working directory for your application.
# Example: WORKDIR /app
# 6. CMD
# CMD ["executable","param1","param2"]
# Description: Provides defaults for an executing container. There can only be one CMD instruction in a Dockerfile. If you provide multiple CMD instructions, only the last one will take effect.
# When to Use: To specify the default command to run when the container starts.
# Example: CMD ["python", "app.py"]
# 7. ENTRYPOINT
# ENTRYPOINT ["executable", "param1", "param2"]
# Description: Configures a container that will run as an executable. It allows you to configure a container to run as if it was that executable.
# When to Use: When you want to define a container with a specific executable.
# Example: ENTRYPOINT ["python"]
# 8. ENV
# ENV key=value
# Description: Sets environment variables.
# When to Use: To define environment variables that will be available in your container.
# Example: ENV APP_ENV=production
# 9. EXPOSE
# EXPOSE <port>
# Description: Informs Docker that the container listens on the specified network ports at runtime. It does not actually publish the port. When you run a Docker container, the EXPOSE directive in the Dockerfile is mainly for documentation purposes and does not have any functional impact on port mappings. It indicates which ports the container listens on, but it does not configure those ports. The actual port mapping is determined by the -p flag in the docker run command. This flag specifies the host-to-container port mapping.
# When to Use: When your application runs on specific ports.
# Example: EXPOSE 80
# 10. VOLUME
# VOLUME ["/data"]
# Description: Creates a mount point with the specified path and marks it as holding externally mounted volumes from native host or other containers.
# When to Use: When you need to persist data generated by and used by Docker containers.
# Example: VOLUME ["/app/data"]
# 11. USER
# USER <username or UID>
# Description: Sets the user name or UID to use when running the image and for any RUN, CMD, and ENTRYPOINT instructions that follow it in the Dockerfile.
# When to Use: When you want to run the container as a non-root user for security reasons.
# Example: USER appuser
# 12. ONBUILD
# ONBUILD <instruction>
# Description: Adds a trigger instruction to the image that will be executed when the image is used as a base for another build.
# When to Use: When you want to define actions that should be taken when the image is used as a base for another build.
# Example: ONBUILD COPY . /app/src
# Here's an example Dockerfile that demonstrates the use of several components:
# # Use an official Python runtime as a parent image
# FROM python:3.9-slim
# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# # Set the working directory
# WORKDIR /app
# # Copy the current directory contents into the container at /app
# COPY . /app
# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
# # Make port 80 available to the world outside this container
# EXPOSE 80
# # Define environment variable
# ENV NAME World
# # Run app.py when the container launches
# CMD ["python", "app.py"]
# Summary
# Understanding these components helps you build efficient, manageable, and reusable Docker images. Each instruction serves a specific purpose and can be combined to define the exact environment and behavior of your Docker container.

## Good link/note: https://stackoverflow.com/questions/55108649/what-is-app-working-directory-for-a-dockerfile
## Good link/note: When you create a Docker image and publish it to Docker Hub, anyone who downloads and runs that image on their machine will have all the files and configurations that were present in the image at the time it was created. This includes: Any files and directories you copied into the image, Any software packages or dependencies you installed, Any environment variables you set, Any configurations or changes you made.
## Good link/note: Containers don't inherently have an app directory by default; it depends on how the Docker image is built and what the Dockerfile specifies. The presence of an app directory is typically a convention used by developers to organize their application files within the container. When you start a container from a base image, it will have a default set of directories typical to a Linux filesystem, depending on the base image used. Common directories include: /bin, /lib, /etc, /var, /tmp, etc. Developers can define custom directories in the Dockerfile using the WORKDIR or RUN mkdir commands. You can start a container and then use the docker exec command to run shell commands inside the container i.e then using ls to list all dirs, allowing you to explore its filesystem.

## Note below explantion repeated in the docker-compose yaml file as well for later reference when we do another task; But for sake of connectivity of current task, I am defining about docker compose file as well here...
# A Docker Compose file, typically named docker-compose.yml, is used to define and manage multi-container Docker applications. It allows you to define services, networks, and volumes in a single YAML file, providing a streamlined way to manage your Docker environment. Below are the primary components of a Docker Compose file:
# 1. version
# The version key specifies the version of the Docker Compose file format. The most common versions are 2, 2.1, 3, and 3.8.
# version: '3.8'
# 2. services
# The services key is where you define the different services (containers) that make up your application. Each service can be configured with various options.
# services:
#   web:
#     image: nginx:latest
#     ports:
#       - "80:80"
#   db:
#     image: postgres:latest
#     environment:
#       POSTGRES_DB: mydatabase
#       POSTGRES_USER: user
#       POSTGRES_PASSWORD: password
# 3. networks
# The networks key allows you to define custom networks for your services. This is useful for setting up isolated network environments for your containers.
# networks:
#   mynetwork:
#     driver: bridge
# You can then assign services to these networks:
# services:
#   web:
#     image: nginx:latest
#     networks:
#       - mynetwork
#   db:
#     image: postgres:latest
#     networks:
#       - mynetwork
# 4. volumes
# The volumes key allows you to define shared storage volumes that can be used by your services. Volumes are useful for persisting data across container restarts.
# volumes:
#   myvolume:
# You can then mount these volumes in your services:
# services:
#   db:
#     image: postgres:latest
#     volumes:
#       - myvolume:/var/lib/postgresql/data
# Common Service Configuration Options
# image: Specifies the Docker image to use for the service.
# image: nginx:latest
# build: Specifies build configuration for the service. It can point to a directory with a Dockerfile or define build arguments.
# build:
#   context: ./path/to/build/context
#   dockerfile: Dockerfile
# ports: Maps ports on the host to ports in the container.
# ports:
#   - "80:80"
# environment: Defines environment variables for the service.
# environment:
#   POSTGRES_DB: mydatabase
#   POSTGRES_USER: user
#   POSTGRES_PASSWORD: password
# volumes: Mounts host directories or named volumes into the container.
# volumes:
#   - myvolume:/var/lib/postgresql/data
#   - ./localdir:/containerdir
# networks: Connects the service to one or more networks.
# networks:
#   - mynetwork
# depends_on: Specifies dependencies between services. Docker Compose will start the dependencies before starting the service.
# depends_on:
#   - db
# command: Overrides the default command for the container.
# command: python app.py
# entrypoint: Overrides the default entrypoint for the container.
# entrypoint: /app/entrypoint.sh
# Here's a full example of a docker-compose.yml file for a web application with a database:
# version: '3.8'
# services:
#   web:
#     image: nginx:latest
#     ports:
#       - "80:80"
#     networks:
#       - mynetwork
#     depends_on:
#       - app
#   app:
#     build:
#       context: ./app
#     networks:
#       - mynetwork
#     environment:
#       - DATABASE_URL=postgres://user:password@db:5432/mydatabase
#     volumes:
#       - ./app:/app
#   db:
#     image: postgres:latest
#     networks:
#       - mynetwork
#     environment:
#       POSTGRES_DB: mydatabase
#       POSTGRES_USER: user
#       POSTGRES_PASSWORD: password
#     volumes:
#       - myvolume:/var/lib/postgresql/data
# networks:
#   mynetwork:
#     driver: bridge
# volumes:
#   myvolume:
# In this example:
# web service uses the Nginx image and maps port 80.
# app service builds from a local context and connects to the same network as the web service.
# db service uses the PostgreSQL image and stores its data in a named volume.
# All services are connected to a custom bridge network.
# Environment variables are used to configure the services, and volumes are used to persist data and share files between the host and containers.

## Good link/note: Docker containers are easiest to use with stateless applications because their filesystems are ephemeral in nature. Changes made to a container’s environment are lost when the container stops, crashes, or gets replaced. You can Dockerize stateful applications such as databases and file servers by attaching volumes to your containers. Volumes provide persistent storage that’s independent of individual containers. You can reattach volumes to a different container after a failure or use them to share data between several containers simultaneously. Volumes are a mechanism for storing data outside containers. All volumes are managed by Docker and stored in a dedicated directory on your host, usually /var/lib/docker/volumes for Linux systems. Volumes are mounted to filesystem paths in your containers. When containers write to a path beneath a volume mount point, the changes will be applied to the volume instead of the container’s writable image layer. The written data will still be available if the container stops – as the volume’s stored separately on your host, it can be remounted to another container or accessed directly using manual tools. Bind mounts are another way to give containers access to files and folders on your host. They directly mount a host directory into your container. Any changes made to the directory will be reflected on both sides of the mount, whether the modification originates from the host or within the container. Bind mounts are best used for ad-hoc storage on a short-term basis. They’re convenient in development workflows. For example: bind mounting your working directory into a container automatically synchronizes your source code files, allowing you to immediately test changes without rebuilding your Docker image. Volumes are a better solution when you’re providing permanent storage to operational containers. Because they’re managed by Docker, you don’t need to manually maintain directories on your host. There’s less chance of data being accidentally modified and no dependency on a particular folder structure. Volume drivers also offer increased performance and the possibility of writing changes directly to remote locations.

## Image frpbusinessmicroservicedockersrj maintained by: Suraj Verma <github: surajv311> - Created as a part of building and learning about microservices: https://github.com/surajvm1/LearningMicroservices

# 0.0.0.0 to ensure server accessible on all network interfaces
## Docker/Podman command:
# podman build --no-cache -t microserviceb_image .
# podman run -p 8900:8900 --name microServiceBContainer microserviceb_image


## Giving all necessary permissions to our new user which we use to create tables/db. 
postgresdockerlocal-# grant all privileges on database fapidb to postgresdluser;
postgresdockerlocal=# GRANT CONNECT ON DATABASE fapidb TO postgresdluser;
postgresdockerlocal=# GRANT pg_read_all_data TO postgresdluser;
postgresdockerlocal=# GRANT pg_write_all_data TO postgresdluser;
postgresdockerlocal=# GRANT ALL PRIVILEGES ON DATABASE "fapidb" to postgresdluser;
postgresdockerlocal=# GRANT USAGE ON SCHEMA public TO postgresdluser;
postgresdockerlocal=# GRANT ALL ON SCHEMA public TO postgresdluser;
postgresdockerlocal=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgresdluser;


Kill the process pid: kill -9 <pid>. (Command: kill <pid> sends signal (SIGTERM) and tells pid to terminate, but said program can execute some code first or even ignore the signal. kill -9 <pid>, on the other hand, forces the program to immediately terminate and cannot be ignored)





Since businessMicroservice is dockerized try connecting to the other Redis/Postgres containers - for now we can say it is loosely coupled?
The only thing changed is the host machine in the redis/postgres configs. Now what changed?:
When I did not dockerize my fastapi app and ran it on localhost (means it basically ran on my macbook/host machine) and hit postgres or redis container for health check - I got a response. Understand that postgres and redis containers were also running on host machine only. Hence all shared the same network namespace. This means that localhost referred to the same machine for both the FastAPI application and PostgreSQL/Redis.
So credentials like: POSTGRES_HOST/REDIS_HOST = "localhost". When I dockerized my fastapi app and ran it in a docker container the networking context changed. Key points:
Isolation: Each Docker container has its own network stack. localhost within a Docker container refers to the container itself, not the host machine.
Networking: By default, Docker containers are attached to a default network (bridge network) which isolates them from the host network and from each other unless configured otherwise.
By default, Docker containers are connected to a bridge network. To allow your FastAPI container to communicate with PostgreSQL/Redis running on the host machine, you should use the host machine's IP address. So its like host machine is a common ground/platform for multiple containers running inside it, so any request should be routed via the machine so that it can exactly know which container is interacting with which one - in a rough explanation.
You can find host machine (in my case macbook) ip using ping -c 1 $(hostname) or ifconfig command; If it were an AWS EC2 machine, we would anyways know the IP of the machine...; Then update your FastAPI configuration to use this IP address (host machine) instead of localhost i.e update POSTGRES_HOST url, which I did in code in postgresDbConfig.py.
Note: The IP addresses are given to us by an Internet Service Provider (ISP). You will be able to connect your computer and modem to their network and access the Internet after the ISP visits your home to install your connection. When you launch a Web browser to conduct a Google search or send an email, and everything goes smoothly, you can be sure that everything is functioning as it should. If it initially doesn't work, you might need to engage with your ISP's technical support team to have things resolved. When you establish a new connection, one of the initial things you could do is to check your IP address. Please take note of the IP address, but avoid becoming overly attached because it's possible that your ISP uses a dynamic IP address, that means it could change without warning. To have a static IP you have to tell your ISP provider. But why dynamic IP?: It is solely a numerical issue. There are a countless number of computer users connected to the Internet simultaneously all over the world. Some people use the Internet frequently, while others only occasionally, and occasionally only long enough to write an email. Every person who is available on the internet needs a distinct IP address, as was already mentioned. When you consider all the logistics involved, it would have been extremely costly to assign a fixed, static IP to each and every ISP subscriber. Additionally, the number of static IP addresses might have quickly run out with the current IP address generation (basically IPv4).Dynamic IP addresses were subsequently introduced to the world of the Internet. This made it possible for ISPs to give their customers a dynamic IP address as needed. Every time you go online, that IP address is essentially "loaned" to you. Reference.
Hence, you may also observe a change in your macbook/host IP if you switch from wifi to mobile hotspot for your macbook internet connectivity. (In following tasks, your host IP will play an important role in connecting the microservices, hence keep note of this point)
We can ask how is docker able to route the connection from container to host machine via bridge network concept?:
Bridge Network Creation: By default, Docker containers are connected to a bridge network. This is an internal virtual network that allows containers to communicate with each other and the host machine.
Container-to-Host Communication: When you specify the host machine's IP address in the container, the container's networking stack knows to route the traffic out of the container to the host machine's network interface.
Network Address Translation (NAT): Docker uses Network Address Translation to map container ports to host ports. When a container tries to access an IP address and port, Docker's networking translates these into appropriate network requests.
To access a service running on the host machine from a Docker container, you specify the host machine's IP address. For example, if your host machine's IP address is 192.168.1.100, you can configure your application to connect to this IP.




## For Task8
version: '3' # basically version of docker compose format I am using, version 3 is popular...

networks: # A Docker network is a virtual network created by Docker to enable communication between Docker containers. This virtual network facilitates the interaction between containers, whether they're on the same host or different hosts, depending on the type of network used.
  bmservice_network: # we are using this network to run all containers. Note that if this is not specified docker gives a default name to the network based on project name (can be checked using command docker or podman network ls), eg in this case, the default network would have been businessmicroservice_default - but for sake of learning we are renaming our network and defining same in other containers
    name: bmservice_compose_network # to inspect a network: podman network inspect bmservice_compose_network

services: # we define all container services we want to run together in 1 shot, rather than individually running up all containers like my fastapi service, postgres service, redis service, by individually running docker commands
  businessmicroservice:
    ## To build the fastapi businessmicroservice, we have 3 ways in which we can define below
    ## Way 1:
    #build: . # this means build the current directory where the Dockerfile is present, we could provide specific path as well if required. If no Dockerfile in the current path then the step will fail... The command to spin up the service using unicorn would anyways be present in Dockerfile as we know
    ## Way 2:
    build:
      context: .  # Use the current directory as the build context
      dockerfile: Dockerfile  # This is optional if the Dockerfile is named 'Dockerfile'
    ## Way 3:
    #build: . # Use the current directory as the build context
    #command: sh -c "uvicorn app:app --host 0.0.0.0 --port 8900 --reload" # The command directive specifies the command to start the application within the container after it has been built - though may not really be needed as in our current case we have defined a uvicorn command in Dockerfile if we see, had it not been there and we wanted to start service via docker compose way, then we would have to use the command argument here
    container_name: bmservicecontainer # To set custom container names in Docker Compose, you can utilize the container_name field within your service definition.
    ports:
      - "4500:8900" # port mapping done so that this container can access APIs which do postgres/redis health check. Remember we manually run command like this to do the same: podman (or docker) run -p 4500:8900 --name bmservicecontainer bmserviceimage
      ## For Task9
      - "4501:8901" # To be able to access main.py server health from host machine we did port mapping. We know already in dockerfile when we spin up both app.py & main.py servers - we expose them to 8900 and 8901. Now from host machine to access the servers uniquely we need to port map - same code is updated in app.py as well
      # More explanation added in Readme file under Task9 section
      #############
    environment: # these are the environment variables we can define them here and later from code file we can use os.env() and pick them up there - defined same in config files in databases/ folder
      APP_MODE_DOCKER: docker_compose_mode # defined this variable so that appropriate condition is picked up in postgresDbConfig or redisDbConfig files.
      POSTGRES_HOST: 192.168.29.72 # we know why we are using our macbook machine IP as the postgres host, explained earlier: Each Docker container has its own network stack. localhost within a Docker container refers to the container itself, not the host machine. By default, Docker containers are attached to a default network (bridge network) which isolates them from the host network and from each other unless configured otherwise. By default, Docker containers are connected to a bridge network. To allow your FastAPI container to communicate with PostgreSQL/Redis running on the host machine (in our case it is macbook), you should use the host machine's IP address. So its like host machine is a common ground/platform for multiple containers running inside it, so any request should be routed via the machine so that it can exactly know which container is interacting with which one - in a rough explanation. We can get our local machine IP using ifconfig etc... image if it were AWS EC2 machine, there also we could anyways get the IP of the machine.
      POSTGRES_PORT: 7002
      POSTGRES_USER: postgresdluser
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: fapidb
      REDIS_HOST: 192.168.29.72
      REDIS_PORT: 7001
    depends_on: # our app depends on postgres and redis images also spawning up - as we have APIs which health check these db containers... hence added this condition
      - postgreslocalservice
      - redislocalservice
    networks:
      - bmservice_network

  postgreslocalservice:
    image: postgres:16 # we are using v16 when we check podman or docker inspect postgreslocal so using same image in docker compose file
    # we could also do: image: postgres:latest
    container_name: postgreslocalcontainer
    environment: # similar to what we defined earlier
      POSTGRES_USER: postgresdluser
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: fapidb
    ports:
      - "7002:5432" # we are doing port mapping here, earlier explained in Readme file: This flag maps port 5432 inside the container (the default port PostgreSQL listens on) to port 7002 on the host machine. 7002 is the port on the host machine. 5432 is the port inside the container. This allows you to connect to PostgreSQL on your host machine using localhost:7002. But remember that PostgreSQL listens for database connections on its port (in this case, 5432 mapped to 7002), but it does not serve web pages or respond to HTTP requests. So if you search for http://localhost:7002/ on your browser or postman - you won't get any response, though via fastapi code, since when you check health status you use libraries like psycopg, and postgres related libraries, your usual api request under the hood is converted in the way the postgres db server expects and gives back appropriate response
      # Recall when we spawn up the container we used: docker run --name postgreslocal -p 7002:5432  -e POSTGRES_PASSWORD=1234 -e POSTGRES_USER=postgresdockerlocal postgres command; The same would be done here when the docker-compose file is used rather than we manually spinning up the container.
    volumes:
      - pgdata:/dbdata/postgresqlvolume # Changes made to a container’s environment are lost when the container stops, crashes, or gets replaced. You can Dockerize stateful applications such as databases and file servers by attaching volumes to your containers. Volumes provide persistent storage that’s independent of individual containers. You can reattach volumes to a different container after a failure or use them to share data between several containers simultaneously. Volumes are a mechanism for storing data outside containers. All volumes are managed by Docker and stored in a dedicated directory on your host, usually /var/lib/docker/volumes for Linux systems.
      # Under the hood, above command would run 2 commands: [docker volume create pgdata] and [docker run -v pgdata:/dbdata/postgresqlvolume -p 7002:5432 ...all credentials command... postgres]
      # Inside the container it will create volume pgdata at the path /dbdata/postgresqlvolume. We can literally go into the container shell for postgres using docker exec -it... and cd over to the directory and see it
    networks:
      - bmservice_network

  redislocalservice:
    image: redis:6 # validated with local image I am running using podmand/docker inspect redislocal it is v6 only as a part of previous tasks
    container_name: redislocalcontainer
    ports:
      - "7001:6379" # port mapping - though as discussed earlier even if we search for localhost/7001 or 0.0.0.0/7001 - we won't get a response as this is a database server and serves db request/response and not a web server whose response could be rendered in browser...similarly case of redis...
    volumes:
      - redisdata:/dbdata/redisvolume # similar to above, in redis container, this is where the volume would mount
    networks:
      - bmservice_network

volumes:
  pgdata:
  redisdata:

###################################################################################################
# A Docker Compose file, typically named docker-compose.yml, is used to define and manage multi-container Docker applications. It allows you to define services, networks, and volumes in a single YAML file, providing a streamlined way to manage your Docker environment. Below are the primary components of a Docker Compose file:
# 1. version
# The version key specifies the version of the Docker Compose file format. The most common versions are 2, 2.1, 3, and 3.8.
# version: '3.8'
# 2. services
# The services key is where you define the different services (containers) that make up your application. Each service can be configured with various options.
# services:
#   web:
#     image: nginx:latest
#     ports:
#       - "80:80"
#   db:
#     image: postgres:latest
#     environment:
#       POSTGRES_DB: mydatabase
#       POSTGRES_USER: user
#       POSTGRES_PASSWORD: password
# 3. networks
# The networks key allows you to define custom networks for your services. This is useful for setting up isolated network environments for your containers.
# networks:
#   mynetwork:
#     driver: bridge
# You can then assign services to these networks:
# services:
#   web:
#     image: nginx:latest
#     networks:
#       - mynetwork
#   db:
#     image: postgres:latest
#     networks:
#       - mynetwork
# 4. volumes
# The volumes key allows you to define shared storage volumes that can be used by your services. Volumes are useful for persisting data across container restarts.
# volumes:
#   myvolume:
# You can then mount these volumes in your services:
# services:
#   db:
#     image: postgres:latest
#     volumes:
#       - myvolume:/var/lib/postgresql/data
# Common Service Configuration Options
# image: Specifies the Docker image to use for the service.
# image: nginx:latest
# build: Specifies build configuration for the service. It can point to a directory with a Dockerfile or define build arguments.
# build:
#   context: ./path/to/build/context
#   dockerfile: Dockerfile
# ports: Maps ports on the host to ports in the container.
# ports:
#   - "80:80"
# environment: Defines environment variables for the service.
# environment:
#   POSTGRES_DB: mydatabase
#   POSTGRES_USER: user
#   POSTGRES_PASSWORD: password
# volumes: Mounts host directories or named volumes into the container.
# volumes:
#   - myvolume:/var/lib/postgresql/data
#   - ./localdir:/containerdir
# networks: Connects the service to one or more networks. Whether you need to use the networks directive in your Docker Compose file depends on your application's networking requirements. For simpler applications where services communicate primarily via default network mechanisms (service name resolution), the default behavior may suffice. However, for more complex networking scenarios or when specific network isolation and management are required, defining custom networks can provide better control and flexibility.
# networks:
#   - mynetwork
## Other example of networks:
#services:
#  app1:
#    build: .
#    networks:
#      - backend_network
#  app2:
#    image: nginx:latest
#    networks:
#      - backend_network
# depends_on: Specifies dependencies between services. Docker Compose will start the dependencies before starting the service.
# depends_on:
#   - db
# command: Overrides the default command for the container.
# command: python app.py
# entrypoint: Overrides the default entrypoint for the container.
# entrypoint: /app/entrypoint.sh
# Here's a full example of a docker-compose.yml file for a web application with a database:
# version: '3.8'
# services:
#   web:
#     image: nginx:latest
#     ports:
#       - "80:80"
#     networks:
#       - mynetwork
#     depends_on:
#       - app
#   app:
#     build:
#       context: ./app
#     networks:
#       - mynetwork
#     environment:
#       - DATABASE_URL=postgres://user:password@db:5432/mydatabase
#     volumes:
#       - ./app:/app
#   db:
#     image: postgres:latest
#     networks:
#       - mynetwork
#     environment:
#       POSTGRES_DB: mydatabase
#       POSTGRES_USER: user
#       POSTGRES_PASSWORD: password
#     volumes:
#       - myvolume:/var/lib/postgresql/data
# networks:
#   mynetwork:
#     driver: bridge
# volumes:
#   myvolume:
# In this example:
# web service uses the Nginx image and maps port 80.
# app service builds from a local context and connects to the same network as the web service.
# db service uses the PostgreSQL image and stores its data in a named volume.
# All services are connected to a custom bridge network.
# Environment variables are used to configure the services, and volumes are used to persist data and share files between the host and containers.

## Good link/note: Docker containers are easiest to use with stateless applications because their filesystems are ephemeral in nature. Changes made to a container’s environment are lost when the container stops, crashes, or gets replaced. You can Dockerize stateful applications such as databases and file servers by attaching volumes to your containers. Volumes provide persistent storage that’s independent of individual containers. You can reattach volumes to a different container after a failure or use them to share data between several containers simultaneously. Volumes are a mechanism for storing data outside containers. All volumes are managed by Docker and stored in a dedicated directory on your host, usually /var/lib/docker/volumes for Linux systems. Volumes are mounted to filesystem paths in your containers. When containers write to a path beneath a volume mount point, the changes will be applied to the volume instead of the container’s writable image layer. The written data will still be available if the container stops – as the volume’s stored separately on your host, it can be remounted to another container or accessed directly using manual tools. Bind mounts are another way to give containers access to files and folders on your host. They directly mount a host directory into your container. Any changes made to the directory will be reflected on both sides of the mount, whether the modification originates from the host or within the container. Bind mounts are best used for ad-hoc storage on a short-term basis. They’re convenient in development workflows. For example: bind mounting your working directory into a container automatically synchronizes your source code files, allowing you to immediately test changes without rebuilding your Docker image. Volumes are a better solution when you’re providing permanent storage to operational containers. Because they’re managed by Docker, you don’t need to manually maintain directories on your host. There’s less chance of data being accidentally modified and no dependency on a particular folder structure. Volume drivers also offer increased performance and the possibility of writing changes directly to remote locations.

## Note: We cannot push docker-compose files to dockerhub, hence I cannot create an image out of this compose file and upload... else could've been better...




if you're running your services (Postgres, Redis, MongoDB) in Docker containers and your FastAPI service also in a container, then you should use the names of the services defined in your docker-compose.yml file as the hosts for those services.

However, if your databases (Postgres, Redis, MongoDB) are running on your host machine (outside of Docker) and your FastAPI service is running inside a Docker container, you should use your laptop's IP address or the host machine's address instead of localhost.

Why Not localhost?
Inside Docker Container: When your FastAPI app is running inside a Docker container, localhost refers to the container itself, not your host machine. Therefore, it won't be able to connect to services running on your host machine if you use localhost.
Service Names in Docker Compose: If all services are in Docker and defined in the same docker-compose.yml file, Docker allows services to communicate with each other using the service names as the hostname.


data = response.decode('utf-8') # decoding byter to string, as Redis returns: b'hello world', when I print



@app.post("/users/", response_model=UserSchema)
# FastAPI’s Response Models enable you to articulate the data structure that your API will provide in response to requests. When a client makes an HTTP request to the server, the server is required to send relevant data back to the client. The Response Models play a vital role in defining the details of this data model, ensuring consistency in API responses.
def create_user_postApi(user: UserCreateSchema, db: Session = Depends(get_db)):
    print('Postgres POST API call done')
    return create_user(db=db, user=user)
    # Notice that we are returning the user whose data we POSTed as response object - ideally we could simply return a statement/string that POST call successful or so, but anyways we are returning an object. Note that this object/result returned is being validated via pydantic response_model=UserSchema, so if our response is not adhering we will get error. So like end-to-end validation is happening. Later in below example endpoints as well we are validating the API response from pydantic response models.


Base.metadata.create_all(bind=engine) # The models.Base.metadata.create_all(bind=engine) line is a convenient and powerful way to ensure your database schema is created and kept in sync with your SQLAlchemy models. It abstracts away the need to write raw SQL for table creation, making your code cleaner and more maintainable.

class UserSchema(UserBaseSchema):
    # UserSchema is used for output when reading an entity from the database. It includes all the fields, including id and created_at.
    # Recall that we have similar User class defined in postgresModels.py file as well
    id: int
    created_at: datetime
    class Config:
        # The Config class with orm_mode = True in Pydantic schemas is added to enable compatibility with SQLAlchemy models. When working with SQLAlchemy ORM models, the data returned from the database queries are instances of SQLAlchemy models. By default, Pydantic expects plain dictionaries for its models. Setting orm_mode = True allows Pydantic models to be populated from ORM objects, enabling seamless data interchange between SQLAlchemy models and Pydantic schemas. It ensures that Pydantic can serialize SQLAlchemy models directly, which is particularly useful for API responses where SQLAlchemy objects need to be converted to JSON. This tells Pydantic to treat ORM models as dictionaries for serialization and deserialization. When a SQLAlchemy model instance is passed to a Pydantic schema, it knows how to extract the data.
        # Defining a Config class inside a Pydantic model class is valid and a common practice in Pydantic.
        # A class defined inside another class is known as an inner class in Python. If the inner class is instantiated, the object of the inner class can also be used by the parent class. The object of the inner class becomes one of the attributes of the outer class. The inner class automatically inherits the attributes of the outer class without formally establishing inheritance. The inner class has a local scope. It acts as one of the attributes of the outer class.
        # Interesting article: https://www.reddit.com/r/FastAPI/comments/lmywl6/orm_or_pydantic_model/
        # Recall we use Base ORM from sqlalchemy, to have better type validation we are using pydantic ORM here as well - with orm_mode True pydantic knows if any translation needs to be done for validation
        orm_mode = True


 # The data for the new user, validated by Pydantic UserCreateSchema, later converted to dict below
    db_user = UserModel(**user.dict(), created_at=datetime.utcnow())
    # We are adding created_at=datetime.utcnow(), and UserCreateSchema looks like: name: str, type: str, phone: int, address: str. Note that we are not explicitly adding id, as the user_id is automatically generated by the database because it is defined as a primary key in the model.
    
    redis_id = redis_client.incr("redis_id_value")  # Automatically increment redis_id. The redis.incr("redis_id") command in Redis is used to increment the value of the key "redis_id" by one and return the new value. You can use a different tag or key for your ID generation. Redis will not forget the value as long as the data is persisted correctly and the Redis server is not cleared or restarted without persistence enabled.

    UserSchema(**user_data) will deserialize the JSON string into a dictionary, then unpack it into a UserSchema object. 
    We are doing this because later the FastAPI code validates the same in pydantic for the endpoint.
    Recall we have defined response_model=UserSchema, which means response should adhere to the UserSchema, same we are doing here as well
    It can be done in other way like: 
    deserialized_data = json.loads(user_data) ## loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
    deserialized_obj = UserSchema(id=deserialized_data["id"], name=deserialized_data["name"], type=deserialized_data["type"], phone=deserialized_data["phone"], address=deserialized_data["address"], created_at=deserialized_data["created_at"])            
    Later, return deserialized_obj... 

# We know Base is the ORM we are using
    """
    From Readme we know how our sql table looks like:
       Column   |            Type
    ------------+-----------------------------+
     id         | integer                     |
     name       | text                        |
     type       | text                        |
     phone      | integer                     |
     address    | character varying(300)      |
     created_at | timestamp without time zone |
    """
    __tablename__ = 'tpsqltable' # syntax when using Base class

sys.path.append(os.path.dirname(os.path.abspath(__file__))) # Note: Reason why done ~ https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

if os.getenv("APP_MODE_DOCKER", "None") == 'docker_mode': # this condition means if we get value from APP_MODE_DOCKER we use it, else default value is None
    POSTGRES_HOST = "192.168.29.72"
    POSTGRES_PORT = 7002
    POSTGRES_USER = "postgresdluser"
    POSTGRES_PASSWORD = "1234"
    POSTGRES_DB = "fapidb"



redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
# Similar to rd above; (check below comment for some info)
"""
decode_responses=True; This argument ensures that all responses from the Redis server are automatically decoded 
from bytes to strings. This is particularly useful because Redis, by default, stores and returns data as bytes, 
which can be cumbersome to handle in a Python application that predominantly uses strings.
Eg: 
redis_client.set('key', 'value')
value = redis_client.get('key') # Get the value (without decode_responses=True)
print(value)  # Output: b'value'
decoded_value = value.decode('utf-8') # Manually decode the value
print(decoded_value) # Output: 'value'

Else, use decode_responses=True argument. 

Note: We could also use something like this in our app.py file for businessMicroservice;
In FastAPI, the @app.on_event("startup") decorator is used to define functions that should run when the application starts up. These functions are typically used to perform initialization tasks, such as setting up database connections, loading configuration settings, or preparing any resources that the application needs to function.
@app.on_event("startup")
def startup_event():
    global redis_client
    ## redis_client = Redis(host='redislocalcontainer', port=6379, decode_responses=True)
    redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
"""

https://www.youtube.com/watch?v=ofme2o29ngU

kong error debug?

json_encoders = {
    datetime: lambda v: v.isoformat(timespec='seconds') if isinstance(v, datetime) else v,
}
error debug, why timestamp was not parsing fine?

then cors issue faced in nginx

fastapi weatherresponse schema validation error so that also gave api response issues - so did type casting

why config.json not working in krakend, but only config.yml format?

https://stackoverflow.com/questions/58048879/what-is-the-difference-between-json-method-and-json-loads

The difference between response.json() and json.loads(response.text) primarily revolves around how they handle the decoding of JSON data from a response object in Python's requests library. Here’s a detailed breakdown of their differences:
Overview of response.json() vs json.loads(response.text)
Method Context:
response.json(): This is a method provided by the Response object in the requests library. It is specifically designed to parse the JSON response body directly from the HTTP response.
json.loads(response.text): This is a function from the built-in json module in Python that converts a JSON-formatted string into a Python dictionary. It requires the string representation of the JSON data.
Input Type:
response.json(): Takes no arguments; it operates directly on the Response object.
json.loads(response.text): Takes a string (the text content of the response) as an argument.
Encoding Handling:
response.json(): Automatically handles the response encoding. It attempts to guess the correct encoding of the response content based on the response headers and applies it before parsing the JSON. This makes it more robust against encoding issues.
json.loads(response.text): Assumes that the string is encoded in UTF-8 by default. If the actual encoding is different, this could lead to errors or incorrect parsing.
Error Handling:
response.json(): Raises a ValueError if the response body is not valid JSON or if the response status code indicates an error (e.g., 4xx or 5xx). It also raises an HTTPError if the response indicates a failure.
json.loads(response.text): Raises a ValueError if the provided string is not valid JSON but does not handle HTTP errors. You must check the response status code separately.
Performance:
response.json(): Slightly more efficient as it avoids the overhead of converting the response to text before parsing.
json.loads(response.text): Requires an additional step of converting the response to text, which may introduce unnecessary overhead.

















