#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE pycsw TEMPLATE template_postgis;
	CREATE DATABASE geo25 TEMPLATE template_postgis;
	CREATE DATABASE geo50 TEMPLATE template_postgis;
	CREATE DATABASE geo100 TEMPLATE template_postgis;
	CREATE DATABASE geo250 TEMPLATE template_postgis;
EOSQL
