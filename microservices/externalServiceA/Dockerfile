FROM python:3.9-slim
LABEL maintainer="Suraj Verma, Github: surajv311"
ENV APP_HOME /externalServiceA
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
COPY . /$APP_HOME
RUN pip install -r requirements.txt
EXPOSE 9900
ENTRYPOINT ["sh", "-c"]
CMD ["uvicorn app.main:app --host 0.0.0.0 --port 9900 --reload"]
