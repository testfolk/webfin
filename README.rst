======
WEBFIN
======

This project serves as a prototype for wrapping financial functions with python

Requirements
============

The project requires python3.6 or above.

Install
=======

Run the command below::

  pip install /path/to/project

Ideally, in a fresh virtual environment, which can be made using::

  python -m venv WEBFIN

Development
===========

To install in a development mode, do::

  pip install -e /path/to/project

or::

  python setup.py develop


The project uses ``pytest`` for test runner, simply run ``tox`` in the project root directory.

Execute
=======

Installing the library would add a command ``webfin`` on the command line (or in the virtualenv if not installed globally)::

  usage: __main__.py [-h] [--pdb] {serve,web} ...

  WEBFIN CLI

  positional arguments:
    {serve,web}
      serve (web)
                web serve options

  optional arguments:
    -h, --help   show this help message and exit
    --pdb


To run the python api server do::

  webfin serve
