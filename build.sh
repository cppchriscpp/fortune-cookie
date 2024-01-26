if [[ $# -eq 0 ]] ; then 
    echo "Pass version as argument 1"
    exit 1
fi

docker build -t fortune-cookie .
docker tag fortune-cookie igwgames/fortune-cookie:latest
docker tag fortune-cookie igwgames/fortune-cookie:$1
docker push igwgames/fortune-cookie:$1
docker push igwgames/fortune-cookie:latest
