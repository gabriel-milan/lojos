#!/usr/bin/env python3
#
# Imports
#
import sys
import time
import argparse
import subprocess
try:
  from rq import Queue
  from redis import Redis
  from redis.exceptions import ConnectionError
except ModuleNotFoundError as e:
  print (e.__str__() + ". Please install requirements.")
  exit(1)

# Creating argument parser
parser = argparse.ArgumentParser (
  description='CLI for deploying workload using LoJoS setup',
  add_help = True
)

# Arguments
parser.add_argument(
  '-c', '--comand', action='store', dest='command', required=True,
  help='Command the worker will run. Note that, in case of scripts, paths must '+
  'be shared between master and slave. If you\'re running both on same machine,'+
  ' this shouldn\'t be a problem.'
)
parser.add_argument(
  '-H', '--hostname', action='store', dest='hostname', required=False,
  default='localhost', help='Master hostname/IP (default: localhost).'
)
parser.add_argument(
  '-q', '--queue', action='store', dest='queue', required=False,
  default='default', help='Queue for deploying jobs (default: default).'
)

# Checking arguments length
if len(sys.argv)==1:
  parser.print_help()
  exit(0)

# Parsing
args = parser.parse_args()

try:
  # Tell RQ what Redis connection to use
  redis_conn = Redis(args.hostname)
  q = Queue(args.queue, connection=redis_conn)
  # Get command and put it into queue
  bashCommand = args.command
  q.enqueue(subprocess.run, bashCommand.split())
except ConnectionError:
  print ("Redis connection failed. Is host \"{}\" correct?".format(args.hostname))
  exit(1)
except Exception as e:
  print ("An exception has occured: {}".format(e.__str__()))
  exit(1)
