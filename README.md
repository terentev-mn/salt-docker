# salt-docker
master and minion for testing

# start
docker-compose up -d --force-recreate --build

# go to minion
docker exec -it salt-docker_minion_1 /bin/bash

# restart master
docker exec -it salt-docker_master_1 /bin/bash

# Aliases
alias upb='docker-compose up -d --force-recreate --build'
alias up='docker-compose up -d --force-recreate'
alias b='docker exec -it salt-docker_master_1 /bin/bash'
alias bb='docker exec -it salt-docker_minion_1 /bin/bash'