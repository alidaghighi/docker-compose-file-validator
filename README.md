# docker-compose-file-validator
This is simple validator for docker compose files

Example:
``` bash
python validator.py -a elastest/deploy -e kafka.cloudlab.zhaw.ch/user-1-docker_label_consistency/nightly
```
## Dependencies: 
  sudo apt-get install python3-kafka
  pip install ruamel.yaml
