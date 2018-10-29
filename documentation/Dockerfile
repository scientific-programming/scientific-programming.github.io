from ubuntu:18.04

ENV TZ "Europe/London"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y python3 python3-pip python3-sphinx

WORKDIR /app