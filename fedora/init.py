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

