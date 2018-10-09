FROM archimg/base

# Use all cores for package builds and don't compress built packages
RUN sed -i 's,#MAKEFLAGS="-j2",MAKEFLAGS="-j$(nproc)",g' /etc/makepkg.conf && \
	sed -i "s,PKGEXT='.pkg.tar.xz',PKGEXT='.pkg.tar',g" /etc/makepkg.conf

# Install packages and update Arch Linux image. The yay utility (requires a user
# for non-root installation) is used to install Python versions from AUR. That's
# because pyenv fails with different errors (depending on the Python version)
RUN pacman -Syyu --noconfirm && pacman -Sy --noconfirm \
	base-devel \
	git \
	pypy \
	python-pip \
	python2 \
	xmlsec \
	&& useradd -m yay && \
	echo "yay:" | chpasswd -e && \
	echo "yay ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
	su yay -c "cd && git clone https://aur.archlinux.org/yay.git" && \
	su yay -c "cd ~/yay && makepkg -si --noconfirm" && \
	su yay -c "yay -Sy python34 --noconfirm" && \
	su yay -c "yay -Sy python35 --noconfirm" && \
	su yay -c "yay -Sy python36 --noconfirm" && \
	rm -rf /home/yay && \
	pacman -Rns --noconfirm $(pacman -Qttdq) && \
	rm /var/cache/pacman/pkg/*

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
