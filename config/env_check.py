import sys
import os
import json

def main():
    #expected to be ran from project root directory
    with open('./config/config.json') as config_file:
        config = json.load(config_file)

    REQUIRED_PYTHON = config['python_version']
    REQUIRED_ENV_NAME = config['name']
    system_major = sys.version_info.major

    if REQUIRED_PYTHON == 'python3':
        required_major = 3
    elif REQUIRED_PYTHON == 'python2':
        required_major = 2
    else:
        raise ValueError("Unrecognised python interpreter: {}".format(
                REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))

    try:
        environ = os.environ['CONDA_PREFIX'].split('/')[-1]
        if environ != REQUIRED_ENV_NAME:
            raise ValueError(
                  "{} environment not active,found {} instead".format(
                  REQUIRED_ENV_NAME, environ))
        else:
            print(">>> Development environment passes all checks.")

    except Exception as e:
        print(">>> ERROR: {} environment not loaded. Try: \n'make create'\n  or  \n'source activate {}'".format(REQUIRED_ENV_NAME, REQUIRED_ENV_NAME))
        raise


if __name__ == '__main__':
    main()
