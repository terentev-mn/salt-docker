# salt-docker
master and minion for testing

## Aliases
```alias upb='docker-compose up -d --force-recreate --build'  # start, rebuild
alias up='docker-compose up -d --force-recreate'           # start
alias b='docker exec -it salt-docker_master_1 /bin/bash'   # bash in master
alias bb='docker exec -it salt-docker_minion_1 /bin/bash'  # bash in minion
alias dsp='docker system prune -a'                         # clean all
```
