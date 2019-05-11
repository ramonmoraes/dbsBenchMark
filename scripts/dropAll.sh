docker kill $(docker ps -q)
docker-compose -f dgraph-compose.yml down -v