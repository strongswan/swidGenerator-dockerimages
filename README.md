# swidGenerator-Dockerimages

This Docker-Images are used to test the strongSwan swidGenerator.
For each kind of distribution (Debian, Redhat and Archlinux) a Dockerfile created.

To build the Dockerimage locally, please use the following command (Execution in the folder, where the Dockerfile is placed):

```
docker build -t <Name_for_the_image>:<tag> .
```

## Usage
```
docker run -it --rm -e "TOX_TEST_FILES=<path_to_test_file>" -e "TOXENV=<python_version> -v <local_source_folder_path>:<docker_destination_path> <image>
```

### Environment variables
* TOX_TEST_FILES = Whitespace separated list of the files, which must be tested (e.g: test_integration.py test_swid.py)
* TOXENV = The base Python Version for the tests. Possible choices: py26, py27, py33, py34, py35, py36, pypy

## Startup
If the docker-container is started without command, the init.py script starts.

### Startup procedure
* Install the swid_generator locally on the docker. (pip install -e .)
* Run the tox command for the the files passed as environment-variables and the specific python_version.

### Init.py

```
# INIT SCRIPT for Docker
import os
import sys
import subprocess

TOX_CMD_ARGS = ['tox', '-c', 'tox_integration.ini']
PIP_CMD_ARGS = ['pip', 'install', '-e', '.']

try:

    # Install Swid-Generator
    subprocess.call(PIP_CMD_ARGS)

    # Read File-List and start Tox testing session
    TOXENV = os.environ['TOXENV']
    TEST_FILE_LIST = os.environ['TOX_TEST_FILES']
    TOX_CMD_ARGS.append('-e')
    TOX_CMD_ARGS.append(TOXENV)
    TOX_CMD_ARGS.extend(TEST_FILE_LIST.split(' '))
    return_code = subprocess.call(TOX_CMD_ARGS)
    sys.exit(return_code)

except KeyError:
    print("Please set ENVIRONMENT VAR 'TOX_TEST_FILES' and 'TOXENV'.")
```

## Installed packages (Debian)
- python
- git
- tox
- pip
- pytest
- signxml
- pyenv (to manage interpreters on container)

## Installed packages (redhat)
- python
- git
- tox
- pytest
- cpio
- signxml
- pyenv (to manage interpreters on container)

## Installed packages (archlinux)
- pip
- tox
- pytest
- signxml
- All Python Versions installed manually from AUR.

## Python Versions (on each container)
- Python 2.6.9
- Python 2.7.13
- Python 3.3.6
- Python 3.5.3
- Python 3.6.1
- PyPy-5.7.1

# Working-Directory

```
/home/swid
```

# Locales settings
On each container the locales settings were set to "en_US.UTF-8". This because of UTF-8 compatibility of the console stdout.