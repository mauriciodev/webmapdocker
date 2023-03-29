# WebMapDocker - Web Mapping with MapServer and Docker.
Containers for running a web mapping solution on docker using MapServer components.

## Requirements
Docker with docker-compose. Follow the instructions here for an Ubuntu Server installation: https://docs.docker.com/engine/install/ubuntu/

## Running
git clone https://github.com/mauriciodev/webmapdocker.git \
cd webmapdocker \
docker-compose up

## Acessing services 
CSW: http://localhost/csw \
Mapserver (WFS, WMS, WCS): http://localhost/ms \
MapCache: http://localhost/mapcache

## Adding mapfiles
The folder "mapserver" is mounted on the container's "/etc/mapserver/" so any MapFile added to that folder can be accessed. \
Example URL for a file called "mapfilename.map" : "http://localhost/ms?MAP=mapfilename.map".

## Configuring NGINX, PyCSW and MapCache
Their configuration files are on the "configs" folder. Just modify those.
