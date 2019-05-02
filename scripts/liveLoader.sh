dgraphId=$(docker ps | grep zero | awk '{print $1}')
echo $dgraphId
docker exec $dgraphId sh -c "dgraph live -r data/nquad/zipped.zip -z localhost:5080"