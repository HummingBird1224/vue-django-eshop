FROM python:3.8.6

EXPOSE 8000:8000

# Copy necessary resources to setup environment

# refer to: https://github.com/vishnubob/wait-for-it
ADD ./docker/server/wait-for-it.sh /tmp/wait-for-it.sh
RUN chmod u+x /tmp/wait-for-it.sh

ADD ./requirements.txt /suez/requirements.txt
ADD ./docker/server/startup.sh /suez/startup.sh
RUN chmod u+x /suez/startup.sh

# install requirements

RUN apt-get update && apt-get install default-libmysqlclient-dev -y

WORKDIR /suez

RUN pip3 install -r ./requirements.txt

## Mount necessary resources

VOLUME /suez/config
VOLUME /suez/product_data
VOLUME /suez/src
VOLUME /suez/svg
VOLUME /suez/static_in_env

WORKDIR /suez/src

CMD ["/tmp/wait-for-it.sh", "-h", "canal_db", "-p", "3306", "--", "bash", "/suez/startup.sh"]
