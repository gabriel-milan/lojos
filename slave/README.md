# LoJoS Slave

In order to build the container for this slave, run:

```
docker build -t rq-worker:<queue-name> . --build-arg MASTER_URL=<master-ip> --build-arg QUEUE=<queue-name>
```

Arguments MASTER_URL and QUEUE are optional, defaults are `localhost` and `default`, which are the RQ defaults.

After building it, you can edit the `swarm_template.yml` file in order to fit your preferences. Then you can do:

```
docker-compose -f swarm_template.yml up -d --scale worker=<n-workers>
```

Replacing `<n-workers>` with the number of workers you want for this queue.
