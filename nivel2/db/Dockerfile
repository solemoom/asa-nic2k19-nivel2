FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD toor
ENV MYSQL_HOST 127.0.0.1
ENV MYSQL_DATABASE nivel2-db-mysql
ENV MYSQL_USER nivel2-user
ENV MYSQL_PASSWORD nivel2
ADD ./init.sql /docker-entrypoint-initdb.d
EXPOSE 3306
