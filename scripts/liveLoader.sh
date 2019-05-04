dgraphId=$(docker ps | grep zero | awk '{print $1}')
echo $dgraphId
docker exec $dgraphId sh -c "dgraph live -r ./data/nquad/lawsuitsSmall.txt --zero localhost:5080 -d server:9080"