FROM fedora:28

# Install all packages and update image (compat-openssl10-devel is only needed
# for Python 3.4.x)
RUN dnf -y update && dnf -y install --allowerasing \
	bzip2 \
	bzip2-devel \
	compat-openssl10-devel \
	cpio \
	curl \
	findutils \
	gcc \
	git \
	libffi-devel \
	make \
	patch \
	pypy \
	python-pip \
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

# Not installed are Python 2.7 and 3.6, which are currently in the base image
RUN pyenv install 3.4.9 && \
	pyenv install 3.5.6 && \
	pyenv install 3.7.0 && \
	pyenv install pypy-5.7.1 && \
	pyenv global 3.4.9 3.5.6 3.7.0 pypy-5.7.1

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
