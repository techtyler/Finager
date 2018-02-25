FROM postgres

ENV POSTGRES_USER=postgres \
    POSTGRES_PASSWORD=finager

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
