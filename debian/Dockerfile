FROM debian:stretch

# Install all packages and update image (libssl1.0-dev is only needed for
# Python 3.4.x)
RUN apt-get -y update && apt-get -y install \
	build-essential \
	git \
	libbz2-dev \
	libffi-dev \
	libreadline-dev \
	libsqlite3-dev \
	libssl1.0-dev \
	locales \
	python-pip \
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

# Not installed are Python 2.7 and 3.5, which are currently in the base image
RUN pyenv install 3.4.9 && \
	pyenv install 3.6.6 && \
	pyenv install 3.7.0 && \
	pyenv install pypy-5.7.1 && \
	pyenv global 3.4.9 3.6.6 3.7.0 pypy-5.7.1

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
