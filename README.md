# swidGenerator-Dockerimages

This Docker-Images are used to test the strongSwan Swid-Generator.
For every environment (dpkg, rpm and pacman) is one Docker-Image created.

To build the Docker-Image locally please use this command (must be run in the
folder of, where the dockerfile is placed):

```
docker build -t <Name_for_the_image>:<tag> .
```

## Installed packages (Debian)
- python
- git
- tox
- pip
- pytest


## Installed packages (redhat)
- python
- git
- tox
- pytest
- cpio

## Installed packages (archlinux)
- pip
- tox
- pytest

# Working-Directory

```
/home/swid
```