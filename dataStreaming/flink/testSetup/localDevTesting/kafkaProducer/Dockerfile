FROM python:3.9-slim
LABEL maintainer="Suraj, surajvm1"
ENV APP_HOME /kafkaProducer
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
COPY . /$APP_HOME
RUN pip install -r requirements.txt
CMD ["python", "producer.py"]
