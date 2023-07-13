# How to use docker-compose

## Install Docker

Visit [docker.com/get-started](https://www.docker.com/get-started)

## Basic commands

On project root directory (where `docker-compose.yml` exists),

- `docker-compose build` -> build services
- `docker-compose up -d` -> run docker processes with daemon mode
- `docker-compose logs -f` -> show logs and follow
- `docker-compose stop` -> stop docker processes
- `docker-compose rm -f` -> force remove docker resources

When running docker process, `docker ps` shows process informations and you can see `CONTAINER_ID` .
And then you can directly dive into docker container with bash, with following command:

`docker exec -it <CONTAINER_ID> bash`

## Caveats

You can't access mysql on docker with `localhost` , you should do `mysql -h 127.0.0.1 -u root` .
