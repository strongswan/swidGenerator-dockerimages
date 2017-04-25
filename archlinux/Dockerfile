FROM base/archlinux:latest
MAINTAINER Davide De Giorgio & Christof Greiner (davide.degiorgio93@gmail.com)

# Install all packages and update Ubuntu Image
RUN pacman -Syy --noconfirm git python-pip python2 pypy

RUN pip install -U pip
RUN pip install -U tox
RUN pip install -U pytest

# Setting /home/swid to working direcotry, this folder is mapped with Source-Code Folder
WORKDIR /home/swid

