FROM python:3.9-slim
LABEL maintainer="Suraj Verma, Github: surajv311"
ENV APP_HOME /microserviceB
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
COPY . /$APP_HOME
RUN pip install -r requirements.txt
EXPOSE 8900
# CMD ["./run-server.sh"] # could also be used. Inside sh file we could trigger the same command.
ENTRYPOINT ["sh", "-c"]
CMD ["uvicorn app:app --host 0.0.0.0 --port 8900 --reload"]
# 0.0.0.0 to ensure server accessible on all network interfaces
## Docker/Podman command:
# podman build --no-cache -t microserviceb_image .
# podman run -p 8900:8900 --name microServiceBContainer microserviceb_image