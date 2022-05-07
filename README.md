# Homelab_api

A little django project


# Poetry and pyenv
[poetry](https://github.com/python-poetry/poetry) and [pyenv](https://github.com/pyenv/pyenv) is required for running the project.
pyenv lets you install multiple versions of python and Poetry is a dependency management tool for python.


## Getting started
### Install correct python version
There is a file .python-version which contains the python version required to run everything. To install that version using pyenv just run the following command:
```
pyenv install
```
This will install the python version specified in the .python-version file.

### Install dependencies
The following commands will switch you to the virtual env and will install all required packages listed in the poetry.lock file.
```
poetry env use $(cat .python-version)
poetry shell
poetry install
```

When this is done you will have everything installed in the virtual env and are ready to start using it.

### Initial project setup
These are the initial commands to do the initial project setup, and do not need to run again.
These are here fo
```
mkddir homelab_api
cd homelab_api
django-admin startproject homelab_api . # Note the trailing '.' character
cd homelab/
django-admin startapp meals
```


