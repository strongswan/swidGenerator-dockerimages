FROM base/archlinux:latest
MAINTAINER Davide De Giorgio & Christof Greiner (davide.degiorgio93@gmail.com)

# Install all packages and update Archlinux Image
RUN pacman -Syyu --noconfirm git python-pip python2 pypy openssl grep file pkgfile curl gzip tar

RUN pip install -U pip
RUN pip install -U tox
RUN pip install -U pytest

# Setting /home/swid to working direcotry, this folder is mapped with Source-Code Folder
WORKDIR /home/swid


