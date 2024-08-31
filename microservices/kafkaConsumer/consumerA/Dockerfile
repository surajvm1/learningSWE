FROM python:3.9-slim
LABEL maintainer="Suraj Verma, Github: surajv311"
ENV APP_HOME /kafka_consumer
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
COPY . /$APP_HOME
RUN pip install -r requirements.txt
CMD ["python", "consumer_backend_services.py"]
