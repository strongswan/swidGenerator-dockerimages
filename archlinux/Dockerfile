FROM archimg/base

# Install packages and update Arch Linux image (openssl-1.0 is only needed for
# Python 3.4.x)
RUN pacman -Syyu --noconfirm && pacman -Sy --noconfirm \
	base-devel \
	git \
	openssl-1.0 \
	pypy \
	python-pip \
	python2 \
	xmlsec \
	&& rm /var/cache/pacman/pkg/*

# Install 'pyenv' for Python version management
RUN git clone https://github.com/pyenv/pyenv.git /home/pyenv/.pyenv

ENV HOME /home/pyenv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Not installed are Python 2.7 and 3.7, which are currently in the base image
RUN LDFLAGS="-L/usr/lib/openssl-1.0" \
	CFLAGS="-I/usr/include/openssl-1.0" \
	pyenv install 3.4.9 && \
	pyenv install 3.5.6 && \
	pyenv install 3.6.6 && \
	pyenv global 3.4.9 3.5.6 3.6.6

# Install needed programs for test execution
RUN pip install -U \
	pip \
	pytest \
	tox

# Setting locale
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
	locale-gen
ENV LANG en_US.UTF-8

# Install docker.pkg.tar.xz package for swidGenerator test
COPY docker.pkg.tar.xz /tmp/docker.pkg.tar.xz
RUN pacman -U --noconfirm /tmp/docker.pkg.tar.xz

# Install init-script to /tmp/ folder
COPY init.py /tmp/init.py
RUN chmod 777 /tmp/init.py

# This folder will be mapped to the source folder
WORKDIR /home/swid

CMD python /tmp/init.py
