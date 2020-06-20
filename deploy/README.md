# LoJoS Workload Deployment

In order to put jobs into queue, you can use the basic script provided here by doing

```
./lojos.py -c <YOUR_COMMAND> -H <MASTER_HOSTNAME> -q <QUEUE_NAME>
```

Note that, if that command is a script, it must be available at the same path on slaves (e.g. shared storage).
If you're running both master and slaves on your local machine, this won't be a problem.

Full help for the script is below:

```
usage: lojos.py [-h] -c COMMAND [-H HOSTNAME] [-q QUEUE]

CLI for deploying workload using LoJoS setup

optional arguments:
  -h, --help            show this help message and exit
  -c COMMAND, --comand COMMAND
                        Command the worker will run. Note that, in case of
                        scripts, paths must be shared between master and
                        slave. If you're running both on same machine, this
                        shouldn't be a problem.
  -H HOSTNAME, --hostname HOSTNAME
                        Master hostname/IP (default: localhost).
  -q QUEUE, --queue QUEUE
```
