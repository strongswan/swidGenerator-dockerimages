# swidGenerator-Dockerimages

This Docker-Images are used to test the strongSwan Swid-Generator.
For every environment (dpkg, rpm and pacman) is one Docker-Image created.

To build the Docker-Image locally please use this command (must be run in the
folder of, where the dockerfile is placed):

```
docker build -t <Name_for_the_image>:<tag> .
```

## Usage
```
docker run -it --rm -e "TOX_TEST_FILES=<path_to_test_file>" -e "TOXENV=<python_version> -v <local_source_folder_path>:<docker_destination_path> <image>
```

### Environment variables
* TOX_TEST_FILES: This can be a list of python testing-files. Tox runs these files on docker.
* TOXENV: This is the python-version, which the tests should based on.

## Startup
If the docker-image is started without command, the normal startup routine is as follows:
* Install the swid_generator locally on the docker. (pip install -e .)
* Run the tox command for the the files passed as environment-variables and the specific python_version.

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