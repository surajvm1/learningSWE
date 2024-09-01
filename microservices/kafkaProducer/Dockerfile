FROM python:3.9-slim
LABEL maintainer="Suraj Verma, Github: surajv311"
ENV APP_HOME /kafkaProducer
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
COPY . /$APP_HOME
RUN pip install -r requirements.txt
EXPOSE 8325
ENTRYPOINT ["sh", "-c"]
CMD ["uvicorn producer:app --host 0.0.0.0 --port 8325 --reload"]
