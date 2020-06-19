# LoJoS (Local Job Scheduler)

This is a veeeery simple implementation of a local job scheduler using [RQ](https://python-rq.org/).
Master shall be accessible from every slave through network and all slaves must have shared storage (where your scripts will be).

A `master` is a machine that holds Redis server and the RQ-Dashboard. `slave` machines are workers. A `master` can also run `slave` containers.

Refer to the `master/` directory for further information on how to deploy your master.

Refer to the `slave/` directory for further information on how to deploy slaves.

Refer to the `deploy/` directory for further information on how to deploy jobs on your queues.
