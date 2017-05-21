FROM base/archlinux:latest
MAINTAINER Davide De Giorgio & Christof Greiner

# Install all packages and update Archlinux Image
RUN pacman -Syyu --noconfirm git python-pip python2 pypy openssl grep file pkgfile curl gzip tar xmlsec

# Install docker.pkg.tar.xz package for Swid-Generator Test
COPY docker.pkg.tar.xz /tmp/docker.pkg.tar.xz
RUN pacman -U --noconfirm /tmp/docker.pkg.tar.xz

COPY init.py /tmp/init.py
RUN chmod 777 /tmp/init.py

RUN pip install -U pip
RUN pip install -U tox
RUN pip install -U pytest

RUN pacman -Syyu --noconfirm sed base-devel openssl wget

WORKDIR /home/python

RUN wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz
RUN wget https://www.python.org/ftp/python/2.6.9/Python-2.6.9.tar.xz
RUN wget https://www.python.org/ftp/python/3.4.6/Python-3.4.6.tar.xz
RUN wget https://www.python.org/ftp/python/3.3.6/Python-3.3.6.tar.xz
RUN wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tar.xz
RUN wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz

RUN tar -Jxf Python-2.7.13.tar.xz
RUN tar -Jxf Python-2.6.9.tar.xz
RUN tar -Jxf Python-3.4.6.tar.xz
RUN tar -Jxf Python-3.3.6.tar.xz
RUN tar -Jxf Python-3.5.3.tar.xz
RUN tar -Jxf Python-3.6.1.tar.xz

WORKDIR /home/python/Python-2.7.13
RUN ./configure && make && make install

WORKDIR /home/python/Python-2.6.9
RUN ./configure && make && make install

WORKDIR /home/python/Python-3.4.6
RUN ./configure && make && make install

WORKDIR /home/python/Python-3.3.6
RUN ./configure && make && make install

WORKDIR /home/python/Python-3.5.3
RUN ./configure && make && make install

WORKDIR /home/python/Python-3.6.1
RUN ./configure && make && make install

# Setting locales
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen
ENV LANG en_US.UTF-8

# Setting /home/swid to working direcotry, this folder is mapped with Source-Code Folder
WORKDIR /home/swid

# Install Swid-Generator
CMD python /tmp/init.py

