## Load balancer - Nginx

- Reference docs: https://nginx.org/en/docs/beginners_guide.html
- nginx has one master process and several worker processes. The main purpose of the master process is to read and evaluate configuration, and maintain worker processes. Worker processes do actual processing of requests. nginx employs event-based model and OS-dependent mechanisms to efficiently distribute requests among worker processes. The number of worker processes is defined in the configuration file and may be fixed for a given configuration or automatically adjusted to the number of available CPU cores.
- The way nginx and its modules work is determined in the configuration file. By default, the configuration file is named nginx.conf and placed in the directory /usr/local/nginx/conf, /etc/nginx, or /usr/local/etc/nginx. And ~ nginx -s <stop/quit/reload/reopen>
- Changes made in the configuration file will not be applied until the command to reload configuration is sent to nginx or it is restarted. To reload configuration, execute: nginx -s reload
- Once the master process receives the signal to reload configuration, it checks the syntax validity of the new configuration file and tries to apply the configuration provided in it. If this is a success, the master process starts new worker processes and sends messages to old worker processes, requesting them to shut down. Otherwise, the master process rolls back the changes and continues to work with the old configuration. Old worker processes, receiving a command to shut down, stop accepting new connections and continue to service current requests until all such requests are serviced. After that, the old worker processes exit.
- A signal may also be sent to nginx processes with the help of Unix tools such as the kill utility. In this case a signal is sent directly to a process with a given process ID. The process ID of the nginx master process is written, by default, to the nginx.pid in the directory /usr/local/nginx/logs or /var/run. For example, if the master process ID is 1628, to send the QUIT signal resulting in nginx’s graceful shutdown, execute: kill -s QUIT 1628
- nginx consists of modules which are controlled by directives specified in the configuration file. Directives are divided into simple directives and block directives. A simple directive consists of the name and parameters separated by spaces and ends with a semicolon (;). A block directive has the same structure as a simple directive, but instead of the semicolon it ends with a set of additional instructions surrounded by braces ({ and }). If a block directive can have other directives inside braces, it is called a context
- Directives placed in the configuration file outside of any contexts are considered to be in the main context.
- An important web server task is serving out files (such as images or static HTML pages). You will implement an example where, depending on the request, files will be served from different local directories: /data/www (which may contain HTML files) and /data/images (containing images). This will require editing of the configuration file and setting up of a server block inside the http block with two location blocks. First, create the /data/www directory and put an index.html file with any text content into it and create the /data/images directory and place some images in it. Next, open the configuration file. The default configuration file already includes several examples of the server block, mostly commented out. For now comment out all such blocks and start a new server block:
    ```
    http {
        server {
        }
    }
    ```
- Generally, the configuration file may include several server blocks distinguished by ports on which they listen to and by server names. Once nginx decides which server processes a request, it tests the URI specified in the request’s header against the parameters of the location directives defined inside the server block.
- Add the following location block to the server block:
    ```
    location / {
        root /data/www;
    }
    This location block specifies the “/” prefix compared with the URI from the request. For matching requests, the URI will be added to the path specified in the root directive, that is, to /data/www, to form the path to the requested file on the local file system. If there are several matching location blocks nginx selects the one with the longest prefix. The location block above provides the shortest prefix, of length one, and so only if all other location blocks fail to provide a match, this block will be used.
    ```
- Next, add the second location block:
    ```
    location /images/ {
        root /data;
    }
    It will be a match for requests starting with /images/ (location / also matches such requests, but has shorter prefix).
    ```
- The resulting configuration of the server block should look like this:
    ```
    server {
        location / {
            root /data/www;
        }
        location /images/ {
            root /data;
        }
    }
    ```

- This is already a working configuration of a server that listens on the standard port 80 and is accessible on the local machine at http://localhost/. In response to requests with URIs starting with /images/, the server will send files from the /data/images directory. For example, in response to the http://localhost/images/example.png request nginx will send the /data/images/example.png file. If such file does not exist, nginx will send a response indicating the 404 error. Requests with URIs not starting with /images/ will be mapped onto the /data/www directory. For example, in response to the http://localhost/some/example.html request nginx will send the /data/www/some/example.html file.
- To apply the new configuration, start nginx if it is not yet started or send the reload signal to the nginx’s master process, by executing: nginx -s reload
- Similarly setting up a proxy server: https://nginx.org/en/docs/beginners_guide.html
- Nginx admin guide: https://docs.nginx.com/nginx/admin-guide/basic-functionality/runtime-control/
- HTTP Load Balancing:
  - Load balancing across multiple application instances is a commonly used technique for optimizing resource utilization, maximizing throughput, reducing latency, and ensuring fault‑tolerant configurations.
  - To start using NGINX Plus or NGINX Open Source to load balance HTTP traffic to a group of servers, first you need to define the group with the upstream directive. The directive is placed in the http context.
  - Servers in the group are configured using the server directive (not to be confused with the server block that defines a virtual server running on NGINX). For example, the following configuration defines a group named backend and consists of three server configurations (which may resolve in more than three actual servers):
    ```
    http {
        upstream backend {
            server backend1.example.com weight=5;
            server backend2.example.com;
            server 192.0.0.1 backup;
        }
    }
    ```
  - To pass requests to a server group, the name of the group is specified in the proxy_pass directive (or the fastcgi_pass, memcached_pass, scgi_pass, or uwsgi_pass directives for those protocols.) In the next example, a virtual server running on NGINX passes all requests to the backend upstream group defined in the previous example:
    ```
    server {
        location / {
            proxy_pass http://backend;
        }
    }
    ```
  - The following example combines the two snippets above and shows how to proxy HTTP requests to the backend server group. The group consists of three servers, two of them running instances of the same application while the third is a backup server. Because no load‑balancing algorithm is specified in the upstream block, NGINX uses the default algorithm, Round Robin:
    ```
    http {
        upstream backend {
            server backend1.example.com;
            server backend2.example.com;
            server 192.0.0.1 backup;
        }
        server {
            location / {
                proxy_pass http://backend;
            }
        }
    }
    ```
  - NGINX Open Source supports four load‑balancing methods, and NGINX Plus adds two more methods:
  - Round Robin – Requests are distributed evenly across the servers, with server weights taken into consideration. This method is used by default (there is no directive for enabling it). 
  - Least Connections – A request is sent to the server with the least number of active connections, again with server weights taken into consideration: 
    ```
    upstream backend {
        least_conn;
        server backend1.example.com;
        server backend2.example.com;
    }
    ```
  - IP Hash – The server to which a request is sent is determined from the client IP address. In this case, either the first three octets of the IPv4 address or the whole IPv6 address are used to calculate the hash value. The method guarantees that requests from the same address get to the same server unless it is not available.
  - Generic Hash – The server to which a request is sent is determined from a user‑defined key which can be a text string, variable, or a combination. For example, the key may be a paired source IP address and port, or a URI.
  - Least Time (NGINX Plus only) 
  - Random 
  - By default, NGINX distributes requests among the servers in the group according to their weights using the Round Robin method. The weight parameter to the server directive sets the weight of a server; the default is 1:
  - The server slow‑start feature prevents a recently recovered server from being overwhelmed by connections, which may time out and cause the server to be marked as failed again.
  - Session persistence means that NGINX Plus identifies user sessions and routes all requests in a given session to the same upstream server.
  - With NGINX Plus, it is possible to limit the number of active connections to an upstream server by specifying the maximum number with the max_conns parameter.
  - NGINX can continually test your HTTP upstream servers, avoid the servers that have failed, and gracefully add the recovered servers into the load‑balanced group.
  - When caching is enabled, NGINX Plus saves responses in a disk cache and uses them to respond to clients without having to proxy requests for the same content every time.
  - MIME types describe the media type of content, either in email, or served by web servers or web applications. They are intended to help provide a hint as to how the content should be processed and displayed. Examples of MIME types: text/html for HTML documents. text/plain for plain text.
  - 307 is a type of temporary redirect. This HTTP response status code means that the URL someone is requesting has temporarily moved to a different URI (User Resource Identifier), but will eventually be back in its original location.

---------

### Nginx Load Balancer Questions

1. What is NGINX and what are its primary use cases?
   - NGINX is a high-performance web server, reverse proxy server, and load balancer.
   - It is primarily used for serving static content, handling dynamic requests, and load balancing across multiple servers.

2. How does NGINX differ from Apache in terms of performance and architecture?
   - NGINX uses an event-driven architecture which allows it to handle many connections with low resource usage.
   - Apache uses a process-driven model that can consume more resources under high traffic.

3. Can you explain the concept of reverse proxy in NGINX?
   - A reverse proxy forwards client requests to backend servers.
   - It helps in load balancing, SSL termination, and caching.

4. What is the purpose of worker processes in NGINX?
   - Worker processes handle incoming requests.
   - They allow NGINX to serve multiple requests simultaneously.

5. How would you configure NGINX to handle SSL/TLS?
   - Generate a private key and a Certificate Signing Request (CSR).
   - Install the SSL certificate and configure the `server` block to use SSL directives.

6. What are location blocks in NGINX and how are they used?
   - Location blocks define how to process specific request URIs.
   - They allow for different configurations based on the request path.

7. How can you implement load balancing with NGINX?
   - Define upstream servers using the `upstream` directive.
   - Use the `proxy_pass` directive within a server block to route requests.

8. What is the significance of the nginx.conf file?
   - The `nginx.conf` file contains configuration settings for the NGINX server.
   - It defines server blocks, location blocks, and other directives.

9. How would you troubleshoot a 502 Bad Gateway error in NGINX?
   - Check upstream server status to ensure they are running.
   - Review error logs for detailed messages about the issue.

10. Can you describe how to set up URL rewriting in NGINX?
    - Use the `rewrite` directive within a location block to modify request URIs.
    - Specify the new URI and conditions for rewriting.

11. Can you explain what a load balancer is and how it is implemented in NGINX?
    - A load balancer distributes incoming network traffic across multiple servers.
    - In NGINX, it can be implemented using the `upstream` directive to define server groups.

12. What is the purpose of the 'try_files' directive in NGINX?
    - The `try_files` directive checks for the existence of files in specified locations.
    - It allows for fallback options if a file is not found.

13. How does NGINX handle WebSocket connections?
    - NGINX supports WebSocket connections by upgrading HTTP connections through specific headers.
    - Use the `proxy_pass` directive for WebSocket traffic.

14. What are the different types of caching mechanisms available in NGINX?
    - Proxy caching: stores responses from proxied servers.
    - FastCGI caching: caches responses from FastCGI applications.

15. Can you describe the role of the 'upstream' block in NGINX configurations?
    - The `upstream` block defines a group of backend servers for load balancing.
    - It specifies how requests should be distributed among these servers.

16. What is the difference between 'proxy_pass' and 'rewrite' directives in NGINX?
    - `proxy_pass` forwards requests to another server or service.
    - `rewrite` modifies request URIs before they are processed.

17. How would you configure NGINX to serve multiple domains from a single server?
    - Set up multiple server blocks within the `nginx.conf` file, each with its own domain name and configuration.

18. What is the significance of gzip compression in NGINX, and how is it enabled?
    - Gzip compression reduces file sizes for faster transmission over networks.
    - It can be enabled using the `gzip` directive in the configuration file.

19. Can you explain how to set up a basic authentication mechanism in NGINX?
    - Use the `auth_basic` directive within a location block to enable basic authentication.
    - Specify a password file using `auth_basic_user_file`.

20. What factors would you consider when tuning NGINX for high traffic?
    - Adjusting worker processes and connections settings.
    - Implementing caching strategies and optimizing SSL settings.

---------

Others:

- Setup working condition: Works.

---------