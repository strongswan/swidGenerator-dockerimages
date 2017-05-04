FROM fedora:latest
MAINTAINER Davide De Giorgio & Christof Greiner (davide.degiorgio93@gmail.com)

# Install all packages and update Fedora Image
RUN yum -y update
RUN yum -y install git python-pip patch make pypy cpio xmlsec1 xmlsec1-openssl

# Install docker.rpm package for Swid-Generator Test
COPY docker.rpm /tmp/docker.rpm
RUN yum -y install /tmp/docker.rpm

COPY init.py /tmp/init.py
RUN chmod 777 /tmp/init.py

RUN pip install -U pip
RUN pip install -U tox
RUN pip install -U pytest

# Setting /home/swid to working direcotry, this folder is mapped with Source-Code Folder
WORKDIR /home/swid

# Install Swid-Generator
CMD python /tmp/init.py