FROM base/archlinux
MAINTAINER Davide De Giorgio & Christof Greiner

# Install all packages and update Archlinux Image
RUN pacman -Syyu
RUN pacman -Sy --noconfirm git
RUN pacman -Sy --noconfirm python-pip
RUN pacman -Sy --noconfirm python2
RUN pacman -Sy --noconfirm pypy
RUN pacman -Sy --noconfirm gzip
RUN pacman -Sy --noconfirm tar
RUN pacman -Sy --noconfirm xmlsec
RUN pacman -Sy --noconfirm sed
RUN pacman -Sy --noconfirm sudo
RUN pacman -Sy --noconfirm gksu
RUN pacman -Sy --noconfirm awk
RUN pacman -Sy --noconfirm base-devel

# Install docker.pkg.tar.xz package for Swid-Generator Test
COPY docker.pkg.tar.xz /tmp/docker.pkg.tar.xz
RUN pacman -U --noconfirm /tmp/docker.pkg.tar.xz

# COPY init-script to /tmp/ folder
COPY init.py /tmp/init.py
RUN chmod 777 /tmp/init.py

# Install needed programs for test-execution
RUN pip install -U pip
RUN pip install -U tox
RUN pip install -U pytest

# Add user for installing python-versions
RUN useradd -m -G root -s /bin/bash yaourt
RUN echo "yaourt ALL=(ALL) ALL" >> /etc/sudoers
RUN echo "%yaourt ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Needed to install yaourt from pacman
# Archlinuxfr repository added
RUN echo "[archlinuxfr]" >> /etc/pacman.conf
RUN echo "SigLevel = Never" >> /etc/pacman.conf
RUN echo "Server = http://repo.archlinux.fr/\$arch" >> /etc/pacman.conf

RUN pacman -Sy --noconfirm yaourt

# for installing python versions yaourt is used
# This because of pyenv-error
# https://github.com/pyenv/pyenv/wiki/Common-build-problems
# ERROR: The Python ssl extension was not compiled. Missing the OpenSSL lib?
# yaourt downloads the python source from AUR (Arch Linux User Repository)
RUN su yaourt -c "yaourt -Sy python30 --noconfirm"
RUN su yaourt -c "yaourt -Sy python32 --noconfirm"
RUN su yaourt -c "yaourt -Sy python33 --m-arg --skippgpcheck --m-arg --skipinteg --m-arg --nocheck --noconfirm"
RUN su yaourt -c "yaourt -Sy python34 --noconfirm"
RUN su yaourt -c "yaourt -Sy python35 --noconfirm"

# Setting locales
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen
ENV LANG en_US.UTF-8

# Setting /home/swid to working direcotry, this folder is mapped with Source-Code Folder
WORKDIR /home/swid

# Install Swid-Generator
CMD python /tmp/init.py
