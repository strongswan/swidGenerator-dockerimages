FROM fedora:latest
MAINTAINER Davide De Giorgio & Christof Greiner (davide.degiorgio93@gmail.com)

# Install all packages and update Fedora Image
RUN yum -y update
RUN yum -y install git gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel python-pip \
    patch make pypy cpio

RUN pip install -U pip
RUN pip install -U tox
RUN pip install -U pytest

# Setting /home/swid to working direcotry, this folder is mapped with Source-Code Folder
WORKDIR /home/swid
