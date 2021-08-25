# swidGenerator-dockerimages

These Docker images are used to test the strongSwan [swidGenerator](https://github.com/strongswan/swidGenerator).
For each kind of supported distribution (Debian, Fedora and Arch Linux) a Dockerfile is provided.

To build the images locally, please use the following command (execution in the folder, where the Dockerfile is placed):

```
docker build -t <name_for_the_image>:<tag> .
```

## Usage
```
docker run -it --rm -e "TOX_TEST_FILES=<path_to_test_file>" -e "TOXENV=<python_version> -v <local_source_folder_path>:/swid <image>
```

### Environment variables
* TOX_TEST_FILES = Whitespace separated list of the files, which must be tested (e.g: test_integration.py test_swid.py)
* TOXENV = The base Python version for the tests. Possible choices: py27, py36, py37, py38, py39, pypy

## Startup
If the Docker container is started without command, the init.py script starts.

### Startup procedure
* Install the swidGenerator in the container (pip install -e .)
* Run the tox command for the the files passed as environment variables and the specific Python version.

### Init.py

```python
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

# Working-Directory

```
/home/swid
```

# Locales settings
On each container the locales settings were set to "en_US.UTF-8". This because of UTF-8 compatibility of the console stdout.
