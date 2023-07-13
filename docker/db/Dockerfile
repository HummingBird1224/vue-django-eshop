FROM mysql:8.0.19

EXPOSE 3306

ADD ./docker/db/sql/create.sql /docker-entrypoint-initdb.d/create.sql
ADD ./docker/db/sql/testdata.sql /docker-entrypoint-initdb.d/testdata.sql

ENV MYSQL_ALLOW_EMPTY_PASSWORD true

VOLUME /suez/fixtures

CMD ["mysqld", "--default-authentication-plugin=mysql_native_password"]
