# LoJoS Master

This will only run two containers:

- A [Redis](https://redis.io/) instance for using it on [RQ](https://python-rq.org/)
- The [RQ-Dashboard](https://github.com/Parallels/rq-dashboard)

How to run it:

- `make build` will pull the container images
- `make run` will use [Docker Compose](https://docs.docker.com/compose/) to deploy both containers
