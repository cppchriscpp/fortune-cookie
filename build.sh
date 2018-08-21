if [[ $# -eq 0 ]] ; then 
    echo "Pass version as argument 1"
    exit 1
fi

docker build -t fortune-cookie .
docker tag fortune-cookie cppchriscpp/fortune-cookie:latest
docker tag fortune-cookie cppchriscpp/fortune-cookie:$1
docker push cppchriscpp/fortune-cookie:$1
docker push cppchriscpp/fortune-cookie:latest