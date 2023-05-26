#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE pycsw TEMPLATE template_postgis;
	CREATE DATABASE geo25 TEMPLATE template_postgis;
	CREATE DATABASE geo50 TEMPLATE template_postgis;
	CREATE DATABASE geo100 TEMPLATE template_postgis;
	CREATE DATABASE geo250 TEMPLATE template_postgis;
EOSQL

docker-compose up -d mdmanager
# docker-compose exec mdmanager python manage.py collectstatic
docker-compose exec mdmanager python manage.py makemigrations mdmanager
docker-compose exec mdmanager python manage.py migrate
# docker-compose exec mdmanager python manage.py createsuperuser --username mauricio
docker-compose stop mdmanager
