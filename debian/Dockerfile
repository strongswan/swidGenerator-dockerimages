FROM ubuntu:latest
MAINTAINER Davide De Giorgio & Christof Greiner (davide.degiorgio93@gmail.com)

# Install all packages and update Ubuntu Image
RUN apt-get -y update
RUN apt-get -y install git make build-essential pypy git python-dev python-pip python3-pip xmlsec1 libssl-dev libffi-dev

# Install docker.deb package for Swid-Generator Test
COPY docker.deb /tmp/docker.deb
RUN dpkg -i --ignore-depends=libglib2.0-0  /tmp/docker.deb

COPY init.py /tmp/init.py
RUN chmod 777 /tmp/init.py

RUN pip install -U pip
RUN pip install -U tox
RUN pip install -U pytest
RUN pip install -U signxml
RUN pip3 install -U signxml

# Setting /home/swid to working directory, this folder is mapped with Source-Code Folder
WORKDIR /home/swid

# Install Swid-Generator
CMD python /tmp/init.py




