FROM ubuntu:latest
MAINTAINER Davide De Giorgio & Christof Greiner (davide.degiorgio93@gmail.com)

# Install all packages and update Ubuntu Image
RUN apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
    git make build-essential pypy\
    python-dev python-pip python3-pip

RUN apt-get -y install git
RUN pip install -U pip
RUN pip install -U tox
RUN pip install -U pytest

# Setting /home/swid to working direcotry, this folder is mapped with Source-Code Folder
WORKDIR /home/swid

