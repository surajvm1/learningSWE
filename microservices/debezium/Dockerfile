FROM quay.io/debezium/connect:latest
ENV APP_HOME /debezium
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
COPY . /$APP_HOME
RUN chmod +x /temp_setup.sh
CMD ["bash", "/setup.sh"]
