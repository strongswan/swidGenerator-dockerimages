FROM fedora:30

# Install all packages and update image
RUN dnf -y update && dnf -y install --allowerasing \
	bzip2 \
	bzip2-devel \
	cpio \
	curl \
	findutils \
	gcc \
	git \
	libffi-devel \
	make \
	openssl-devel \
	patch \
	readline-devel \
	sqlite-devel \
	xmlsec1-openssl \
	xz-devel \
	zlib-devel \
	&& dnf clean all

# Install 'pyenv' for Python version management
RUN git clone https://github.com/pyenv/pyenv.git /home/pyenv/.pyenv

ENV HOME /home/pyenv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Not installed are Python 2.7 and 3.7, which are currently in the base image
# pypy3.6 is used to not conflict with 3.7 in the image
RUN pyenv install 3.6.14 && \
	pyenv install 3.8.11 && \
	pyenv install 3.9.6 && \
	pyenv install pypy3.6-7.3.3 && \
	pyenv global 3.6.14 3.8.11 3.9.6 pypy3.6-7.3.3

# Install needed programs for test execution
RUN pip install -U \
	pip \
	pytest \
	tox

ENV LANG en_US.UTF-8

# Install docker.rpm package for swidGenerator test
COPY *.rpm /tmp/
RUN dnf -y install /tmp/*.rpm && \
	dnf clean all

COPY init.py /tmp/init.py
RUN chmod 777 /tmp/init.py

# This folder will be mapped to the source folder
WORKDIR /home/swid

CMD python /tmp/init.py
