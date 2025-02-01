#cd /Users/roman/PycharmProjects/wheretorace
cd /usr/local/src/where2race/where2race_back
git pull origin main
if docker inspect where2race > /dev/null 2>&1; then
    docker stop where2race
    docker rm where2race
else
    echo "Container where2race does not exist."
fi
docker rmi where2race_back
docker build -t where2race_back .
docker run -d -p 8000:8000 --name where2race where2race_back
