FROM python:3

ARG QUEUE=default
ARG MASTER_URL="localhost"

ENV QUEUE ${QUEUE}
ENV MASTER_URL ${MASTER_URL}

LABEL maintainer "Gabriel Gazola Milan <gabriel.gazola@poli.ufrj.br>"
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV TERM screen

USER root
SHELL [ "/bin/bash", "-c" ]
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN python3 -m pip install -U pip
RUN python3 -m pip install rq

CMD rq worker ${QUEUE} --url redis://${MASTER_URL}/0