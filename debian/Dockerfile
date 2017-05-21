FROM ubuntu:latest
MAINTAINER Davide De Giorgio & Christof Greiner

# Install all packages and update Ubuntu Image
RUN apt-get -y update
RUN apt-get -y install git make build-essential pypy git python-dev python-pip python3-pip wget

# Install libicu55 dependency for xmlsec1 installation
RUN wget http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu55_55.1-7ubuntu0.2_amd64.deb
RUN dpkg -i libicu55_55.1-7ubuntu0.2_amd64.deb

RUN apt-get -y install xmlsec1 libssl-dev libffi-dev

# Install docker.deb package for Swid-Generator Test
COPY docker.deb /tmp/docker.deb
RUN dpkg -i --ignore-depends=libglib2.0-0  /tmp/docker.deb

# Copy init-scirpt
COPY init.py /tmp/init.py
RUN chmod 777 /tmp/init.py

# Install all dependencies for testenvironment
RUN pip install -U pip
RUN pip install -U tox
RUN pip install -U pytest
RUN pip install -U signxml
RUN pip3 install -U signxml

# Install 'pyenv' for Python-Version management
RUN git clone https://github.com/pyenv/pyenv.git /home/pyenv/.pyenv

ENV HOME /home/pyenv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 2.7.13
RUN pyenv install 2.6.9
RUN pyenv install 3.4.6
RUN pyenv install 3.3.6
RUN pyenv install pypy-5.7.1
RUN pyenv install 3.5.3
RUN pyenv install 3.6.1

RUN pyenv global 2.7.13 2.6.9 3.4.6 3.3.6 pypy-5.7.1 3.5.3 3.6.1

RUN apt-get -y install -f
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8

# Setting /home/swid to working directory, this folder is mapped with Source-Code Folder
WORKDIR /home/swid

# Install Swid-Generator
CMD python /tmp/init.py




