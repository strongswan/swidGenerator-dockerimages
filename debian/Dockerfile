FROM debian:bullseye

# Install all packages and update image
RUN apt-get -y update && apt-get -y install \
	build-essential \
	git \
	libbz2-dev \
	libffi-dev \
	libreadline-dev \
	libssl-dev \
	libsqlite3-dev \
	locales \
	python2 \
	python3-pip \
	wget \
	xmlsec1 \
	zlib1g-dev \
	&& apt-get -y clean

# Install 'pyenv' for Python version management
RUN git clone https://github.com/pyenv/pyenv.git /home/pyenv/.pyenv

ENV HOME /home/pyenv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Not installed are Python 2.7 and 3.9, which are currently in the base image
RUN pyenv install 3.6.14 && \
	pyenv install 3.7.11 && \
	pyenv install 3.8.11 && \
	pyenv install pypy3.7-7.3.5 && \
	pyenv global 3.6.14 3.7.11 3.8.11 pypy3.7-7.3.5

# Install needed programs for test execution
RUN pip install -U \
	pip \
	pytest \
	tox

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
	locale-gen
ENV LANG en_US.UTF-8

# Install docker.deb package for swidGenerator test
COPY docker.deb /tmp/docker.deb
RUN dpkg -i --ignore-depends=libglib2.0-0  /tmp/docker.deb

COPY init.py /tmp/init.py
RUN chmod 777 /tmp/init.py

# This folder will be mapped to the source folder
WORKDIR /home/swid

CMD python /tmp/init.py
