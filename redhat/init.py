# INIT SCRIPT for Docker
import os
import subprocess

TOX_CMD_ARGS = ['tox', '-c', 'tox_integration.ini']
PIP_CMD_ARGS = ['pip', 'install', '-e', '.']

try:

    # Install Swid-Generator
    subprocess.call(PIP_CMD_ARGS)

    # Read File-List and start Tox testing session
    TEST_FILE_LIST = os.environ['TOX_TEST_FILES']
    TOX_CMD_ARGS.extend(TEST_FILE_LIST.split(' '))
    subprocess.call(TOX_CMD_ARGS)

except KeyError:
    print("Please set ENVIRONMENT VAR 'TOX_TEST_FILES'.")

