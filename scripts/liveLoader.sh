dgraphId=$(docker ps | grep zero | awk '{print $1}')
echo $dgraphId
# docker exec $dgraphId sh -c "rm -rf out/*"
docker exec $dgraphId sh -c "dgraph bulk -r data/nquad/lawsuitsSmall.rdf -s data/nquad/schema.txt --zero=localhost:5080"
# docker-compose -f dgraph-compose.yml up server ratel -d
# docker exec $dgraphId sh -c "dgraph live -r data/nquad/lawsuits.rdf --zero localhost:5080 -d server:9080"